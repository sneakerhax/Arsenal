# Docker - Nmap (Kali Linux)

A Dockerized version of the tool Nmap

## Building the image

```docker build -t nmap .```

## Running the container

```docker run -it nmap <parameter> <target>```

Run nmap with parameters

## Using nse search function

```bash
docker run -it --entrypoint=bash nmap
┌──(root💀f15991a37109)-[/]
└─# nse smb
smb-security-mode.nse
smb2-vuln-uptime.nse
smb-print-text.nse
---truncated---
```

Search for nse modules that contain smb
