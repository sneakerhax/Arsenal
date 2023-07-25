import json
import os
import requests
import subprocess
import sys

domain_list = []

# Censys.io access
censys_API_ID = os.getenv('censys_API_ID')
censys_secret = os.getenv('censys_secret')
censys_basic_auth = (censys_API_ID, censys_secret)

# Amass binary and output file
amass_binary = "amass_Linux_amd64/amass"
amass_output = "amass_dns.txt"

# CRTSH command - curl -s "https://crt.sh/?q=uipath.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u > certsh.txt


def usage():
    print("[*] Usage - python3 PyDNSRecon.py <target>")


def banner():
    print("    ____        ____  _   _______ ____")
    print("   / __ \__  __/ __ \/ | / / ___// __ \___  _________  ____")
    print("  / /_/ / / / / / / /  |/ /\__ \/ /_/ / _ \/ ___/ __ \/ __ \\")
    print(" / ____/ /_/ / /_/ / /|  /___/ / _, _/  __/ /__/ /_/ / / / /")
    print("/_/    \__, /_____/_/ |_//____/_/ |_|\___/\___/\____/_/ /_/")
    print("      /____/")
    print("")
    print("by: sneakerhax")
    print("")


def censys_cert_search(censys_target, domain_list):
    print("[+] Running Censys.io certificate search on " + str(censys_target))
    url = "https://search.censys.io/api/v2/certificates/search?q=" + censys_target
    response = requests.request("GET", url, auth=censys_basic_auth)
    json_response = response.json()
    for result in json_response['result']['hits'][0]['names']:
        if censys_target in result:
            domain_list.append(result.strip())


def amass_dns_active(amass_target, amass_output, domain_list):
    print("[+] Running Amass active scan on " + amass_target)
    amass = subprocess.Popen([amass_binary, 'enum', '-d', amass_target, '-o', amass_output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    amass.communicate()
    with open(amass_output, 'r') as amass_open:
        for result in amass_open:
            domain_list.append(result.strip())


def crtsh_cert_search(crtsh_target, domain_list):
    print("[+] Running Crt.sh certificate search for " + crtsh_target)
    crtsh_search = f"https://crt.sh/?q={crtsh_target}&output=json"
    response = requests.get(crtsh_search).json()
    for result in response:
        if "\n" in result['name_value']:
            split_items = result['name_value'].split('\n')
            for item in split_items:
                domain_list.append((item.strip()))
        else:
            domain_list.append((result['name_value'].strip()))


def run(target):
    try:
        censys_cert_search(target, domain_list)
    except Exception as e:
        print("[-] Error running Censys certificate search")
        pass
    try:
        amass_dns_active(target, amass_output, domain_list)
    except Exception as e:
        print("[-] Error running Amass DNS active scan")
        pass
    try:
        crtsh_cert_search(target, domain_list)
    except Exception as e:
        print("[-] Error running CRT.sh certificate search")
        pass

    unique_domains = set(domain_list)
    print("[+] Printing " + str(len(unique_domains)) + " discovered DNS records")
    for domain in unique_domains:
        print(domain.strip())


def main():
    if len(sys.argv) == 2:
        banner()
        target = sys.argv[1]
        run(target)
    else:
        banner()
        usage()


if __name__ == '__main__':
    main()
