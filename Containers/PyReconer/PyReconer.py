import subprocess
import sys

# Tool locations
amass_binary = "amass/amass"
eyewitness_binary = "EyeWitness/Python/EyeWitness.py"
nmap_binary = "nmap"
python_binary = "python3"

# Output files
amass_output = "output/amass_results.txt"
nmap_output = "output/nmap_results"
nmap_output_xml = "output/nmap_results.xml"
eyewitness_output = "output/eyewitness"


def banner():
    print("    ____        ____")
    print("   / __ \__  __/ __ \___  _________  ____  ___  _____")
    print("  / /_/ / / / / /_/ / _ \/ ___/ __ \/ __ \/ _ \/ ___/")
    print(" / ____/ /_/ / _, _/  __/ /__/ /_/ / / / /  __/ /")
    print("/_/    \__, /_/ |_|\___/\___/\____/_/ /_/\___/_/")
    print("      /____/")
    print("")
    print("by: sneakerhax")
    print("")


def usage():
    print("python3 PyReconer.py <target>")


def amass_dns_active(amass_targets, amass_output):
    print("[+] Running amass on " + amass_targets)
    amass = subprocess.Popen([amass_binary, 'enum', '-r', '1.1.1.1', '-o', amass_output, '-d', amass_targets], stdout=subprocess.PIPE)
    out, err = amass.communicate()
    print(out.decode('utf-8'))


def nmap_top_ports(nmap_targets, nmap_output):
    print("[+] Running nmap on " + amass_output)
    nmap = subprocess.Popen([nmap_binary, '--unprivileged', '--top-ports', '1000', '-Pn', '--open', '--reason', '-iL', nmap_targets, '-oA', nmap_output], stdout=subprocess.PIPE)
    out, err = nmap.communicate()
    print(out.decode('utf-8'))


def eyewitness_screen_grab(nmap_output_xml):
    print("[+] Running eyewitness on " + nmap_output_xml)
    eyewitness_run = subprocess.Popen([python_binary, eyewitness_binary, '-x', nmap_output_xml, '--web', '-d', eyewitness_output, '--no-prompt'], stdout=subprocess.PIPE)
    out, err = eyewitness_run.communicate()
    print(out.decode('utf-8'))


def main():
    if len(sys.argv) == 2:
        banner()
        target = sys.argv[1]
        amass_dns_active(target, amass_output)
        nmap_top_ports(amass_output, nmap_output)
        eyewitness_screen_grab(nmap_output_xml)
    else:
        banner()
        usage()


if __name__ == "__main__":
    main()
