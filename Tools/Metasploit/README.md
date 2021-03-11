# Docker - Metasploit (Kali Linux)

A Dockerized version of the tool Metasploit

## Building the image

```docker build -t metasploit .```

The initial build can take 10-15 minutes

## Running the container

```docker run -it metasploit```

Runs msfstart.sh and drops into msfconsole