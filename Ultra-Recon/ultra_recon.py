import argparse
import configparser
import docker
from pathlib import Path


def banner():
    print("    __  ______                ____")
    print("   / / / / / /__________ _   / __ \___  _________  ____")
    print("  / / / / / __/ ___/ __ `/  / /_/ / _ \/ ___/ __ \/ __ \\")
    print(" / /_/ / / /_/ /  / /_/ /  / _, _/  __/ /__/ /_/ / / / /")
    print(" \____/_/\__/_/   \__,_/  /_/ |_|\___/\___/\____/_/ /_/")
    print("")
    print("\t by sneakerhax...")
    print("")


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
    config = configparser.ConfigParser()
    config.read('config.conf')
    censys_API_ID = config['censys.io']['censys_API_ID']
    censys_secret = config['censys.io']['censys_secret']

    # Tool file
    tool_dir = Path('tools', args.image)

    # Build Docker image with Docker SDK for Python
    client = docker.from_env()
    print("[+] Building image " + str(args.image))
    if Path.exists(tool_dir):
        client.images.build(path=str(tool_dir), tag=args.image)
    else:
        print("[-] Path to Dockerfile does not exist")
        exit()

    # Target output file check and creation
    output_dir = Path('output', args.name)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Run Docker container with Docker SDK for Python
    print("[+] Starting container " + str(args.image))
    target = args.target
    if args.image == "nmap":
        container_output = client.containers.run(args.image, command=target + " -p 80")
    if args.image == "pydnsrecon":
        container_output = client.containers.run(args.image, command=target, environment=["censys_API_ID=" + censys_API_ID, "censys_secret=" + censys_secret])

    # Output container stdout to output folder
    outputpath = Path(output_dir, args.image + ".txt")
    print("[+] writing output to " + str(outputpath))
    with open(outputpath, 'w') as out:
        out.write(container_output.decode())


if __name__ == '__main__':
    main()
