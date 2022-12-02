# Docker - PyReconer

A Dockerized tool written in Python to perform recon

## Building the image

```
docker build -t pyreconer .
```
Build the PyReconer image (takes around 220s on my M1 Macbook Pro)

## Running the container

```
docker run --platform=linux/x86_64 -v output:/PyReconer/output -it pyreconer <target>
```

If you're using Apple silicon (M1/M2) you should set the --platform arguments as seen above.

## Sample Usage

```
$ docker run --platform=linux/x86_64 -v output:/PyReconer/output -it pyreconer scanme.nmap.org
    ____        ____
   / __ \__  __/ __ \___  _________  ____  ___  _____
  / /_/ / / / / /_/ / _ \/ ___/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / _, _/  __/ /__/ /_/ / / / /  __/ /
/_/    \__, /_/ |_|\___/\___/\____/_/ /_/\___/_/
      /____/

by: sneakerhax

[+] Running amass on scanme.nmap.org

OWASP Amass v3.0.4                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
1 names discovered - dns: 1
--------------------------------------------------------------------------------
ASN: 63949 - LINODE-AP Linode
	45.33.32.0/24     	1    Subdomain Name(s)
scanme.nmap.org

[+] Running nmap on output/amass_results.txt

Starting Nmap 7.40 ( https://nmap.org ) at 2019-07-08 21:34 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up, received user-set (0.030s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
Reason: 996 resets
PORT      STATE SERVICE    REASON
22/tcp    open  ssh        syn-ack ttl 49
80/tcp    open  http       syn-ack ttl 50
9929/tcp  open  nping-echo syn-ack ttl 50
31337/tcp open  Elite      syn-ack ttl 49

Nmap done: 1 IP address (1 host up) scanned in 1.73 seconds

[+] Running Eywitness on output/nmap_results.xml
################################################################################
#                                  EyeWitness                                  #
################################################################################
#           FortyNorth Security - https://www.fortynorthsecurity.com           #
################################################################################

Starting Web Requests (1 Hosts)
Attempting to screenshot http://scanme.nmap.org
Finished in 27.50956964492798 seconds
```

## List of 3rd party tools

* [Amass](https://github.com/OWASP/Amass) - OWASP
* [Nmap](https://nmap.org/) - Fyador and contributors
* [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness) - christophertruncer

