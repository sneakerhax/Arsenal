import argparse
import configparser
import datetime
import docker
import sys
from git import Repo
from os import system
from pathlib import Path
from urllib.parse import urlparse


def banner():
    print("    __  ______                ____")
    print("   / / / / / /__________ _   / __ \___  _________  ____")
    print("  / / / / / __/ ___/ __ `/  / /_/ / _ \/ ___/ __ \/ __ \\")
    print(" / /_/ / / /_/ /  / /_/ /  / _, _/  __/ /__/ /_/ / / / /")
    print(" \____/_/\__/_/   \__,_/  /_/ |_|\___/\___/\____/_/ /_/")
    print("")
    print("\t by sneakerhax...")
    print("")


def extract_hostname(target):
    target = urlparse(target).netloc
    return target


def main():

    # print banner
    banner()

    # parse arguments
    parser = argparse.ArgumentParser(description='Ultra Recon')
    parser.add_argument('-n', '--name', required=True, action='store', dest='name', type=str, help='Target name')
    parser.add_argument('-t', '--target', required=True, action='store', dest='target', type=str, help='Target to scan')
    parser.add_argument('-i', '--image', required=True, action='store', dest='image', type=str, help="Name of Image")
    parser.add_argument('-c', '--command', action='store', dest='command', type=str, help="Command to pass")
    args = parser.parse_args()

    # load config
    try:
        config = configparser.ConfigParser()
        config.read('config.conf')
        censys_API_ID = config['censys.io']['censys_API_ID']
        censys_secret = config['censys.io']['censys_secret']
    except Exception as e:
        print("[-] Failed to load config file")

    # Tool file
    tool_dir = Path('../', args.image)

    # Connect to the Docker daemon
    try:
        client = docker.from_env()
    except Exception as e:
        print("[-] Failed when connecting to Docker daemon")
        sys.exit()

    # Check for dirsearch folder and if it exist delete before cloning the tool repo
    if args.image == "dirsearch":
        if Path.exists(Path(tool_dir)):
            print("[+] Pulling Dirsearch Github repo")
            repo = Repo("../Dirsearch")
            origin = repo.remotes.origin
            origin.pull()
        else:
            print("[+] Cloning Dirsearch Github repo")
            Repo.clone_from("https://github.com/maurosoria/dirsearch.git", "../Dirsearch")

    # Build Docker image with Docker SDK for Python
    print("[+] Building image " + str(args.image))
    if Path.exists(tool_dir):
        client.images.build(path=str(tool_dir), rm=True, tag=args.image)
    else:
        print("[-] Path to Dockerfile does not exist")
        sys.exit()

    # Target output file check and creation
    output_dir = Path('output', args.name)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Run Docker container with Docker SDK for Python
    now_scan_start = datetime.datetime.now()
    print("[*] Starting Scan at " + now_scan_start.strftime("%m-%d-%Y_%H:%M:%S"))
    print("[+] Running container " + str(args.image) + " on target " + str(args.target))
    target = args.target
    if args.image == "nmap":
        container_output = client.containers.run(args.image, remove=True, command=target)
    if args.image == "nmap-small":
        container_output = client.containers.run(args.image, remove=True, command=target)
    if args.image == "pydnsrecon":
        container_output = client.containers.run(args.image, remove=True, command=target, environment=["censys_API_ID=" + censys_API_ID, "censys_secret=" + censys_secret])
    if args.image == "pydnsrecon-passive":
        container_output = client.containers.run(args.image, remove=True, command=target, environment=["censys_API_ID=" + censys_API_ID, "censys_secret=" + censys_secret])
    if args.image == "pydnsrecon-m1":
        container_output = client.containers.run(args.image, remove=True, command=target, environment=["censys_API_ID=" + censys_API_ID, "censys_secret=" + censys_secret])
    if args.image == "whatweb":
        container_output = client.containers.run(args.image, remove=True, command=["--color=never", target])
    if args.image == "dirsearch":
        container_output = client.containers.run(args.image, remove=True, command=["--no-color", "-q", "-u", target])
        # container_output = client.containers.run(args.image, remove=True, command=["--no-color", "--help"])
        target = extract_hostname(target)
    now_scan_end = datetime.datetime.now()
    print("[*] Finished Scan at " + now_scan_end.strftime("%m-%d-%Y_%H:%M:%S"))

    # Output container stdout to output folder
    outputpath = Path(output_dir, target + "_" + args.image + "_" + now_scan_end.strftime("%m-%d-%Y_%H:%M:%S") + ".txt")
    print("[+] Writing output to " + str(outputpath))
    with open(outputpath, 'w') as out:
        out.write(container_output.decode())


if __name__ == '__main__':
    main()
