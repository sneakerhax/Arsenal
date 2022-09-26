# Docker - Metasploit (Kali Linux)

A Dockerized version of the tool Metasploit

## Running with Docker (Local build)

```
docker build -t metasploit .
```

The initial build can take 10-15 minutes (locally)

```
docker run -it metasploit
```

Runs msfstart.sh and drops into msfconsole

## Running with Docker (Docker Hub)

```
docker run -it sneakerhax/metasploit
```

Start image pulled from Docker Hub and run Metasploit
