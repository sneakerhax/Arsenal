# Docker - Nmap (Kali Linux)

A Dockerized version of the tool Nmap

## Running with Docker (Local build)

```docker build -t nmap .```

Build the container

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

## Running with Docker (Docker Hub)

```docker run -it sneakerhax\nmap <parameters> <targets>```
