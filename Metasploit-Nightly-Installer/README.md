# Docker - Metasploit (Nightly Installer)

A Dockerized version of the Metasploit Nightly Installer

## Running with Docker (Local build)

```
docker build -t metasploit_nightly_installer .
```

The initial build can take 10-15 minutes (locally)

```
docker run -it metasploit_nightly_installer
```

Runs msfstart.sh and drops into msfconsole
