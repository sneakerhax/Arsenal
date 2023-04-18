# Offensive Containers

Leveraging container technologies to build offensive security tools

## Containerized Offensive Security Tools

Containers are an effective way to configure, deploy, and use offensive security tools. 

Containerizing offensive security tools provides the following benefits:

* Consistent setup and configuration (Single command builds)
* Documented setup process (Dockerfiles)
* Deployable to cloud services (e.g. recon scans, c2 infra, team services)

For more information on Containerizing tools check out these [resources](https://github.com/sneakerhax/Arsenal/blob/main/Tools/Docker/README.md)

## Docker (Building and Running locally)

```
docker build -t <image_name> <tool_directory>
```

Building one of the tools using the Dockerfile in each tool directory

```
docker run -it <image_name> <arguments>
```
Running the tool after building the image

## Images

* C2concealer
* Dirbpy
* Dirsearch
* Emailharvester
* FFuF
* HardCIDR
* Infra
    * socat-http-redirector
* Kali-Linux
* Linode_cli
* Metasploit
* Metasploit Nightly Installer (deprecated)
* Ncrack
* Ngrok (instructions only)
* Nmap (Includes ncrack)
* Nmap-small
* PyDNSRecon
* PyDNSRecon-Passive
* PyDNSRecon-m1
* Pyfiscan
* PyReconer
* Searchsploit
* Shodan
* Ultra-Recon
* WhatWeb
* Wordlists

## Docker Hub

Tools Containerized through autobuilds on Docker Hub can be found [here](https://hub.docker.com/u/sneakerhax)

```
docker run it sneakerhax\<image_name> <arguments>
```
Running a tool listed on Docker Hub

## Ultra Recon

Additionally, some of the tools are automated using the Docker SDK for Python

```
$ Ultra-Recon % python3 Ultra-Recon/ultra_recon.py -n sample -t scanme.nmap.org -i nmap
    __  ______                ____
   / / / / / /__________ _   / __ \___  _________  ____
  / / / / / __/ ___/ __ `/  / /_/ / _ \/ ___/ __ \/ __ \
 / /_/ / / /_/ /  / /_/ /  / _, _/  __/ /__/ /_/ / / / /
 \____/_/\__/_/   \__,_/  /_/ |_|\___/\___/\____/_/ /_/

	 by sneakerhax...

[+] Building image nmap
[*] Starting Scan at 11-03-2021_13:34:35
[+] Running container nmap on target scanme.nmap.org
[*] Finished Scan at 11-03-2021_13:34:38
[+] Writing output to output/10.0.0.1/scanme.nmap.org_nmap_11-03-2021_13:34:38.txt
```

Running Nmap with Ultra-Recon. The output will be in the Ultra-Recon output directory
