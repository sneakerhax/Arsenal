# Docker - Nmap (Alpine)

A Dockerized version of the tool Nmap that is smaller and works on Raspberry pi

## Running with Docker (Local build)

```docker build -t nmap-small .```

Build the container (locally)

```docker run -it nmap-small <arguments> <target>```

Run nmap with arguments

## Running with Docker (Docker Hub)

```docker run -it sneakerhax\nmap-small <arguments> <targets>```

Start image pulled from Docker Hub and run Nmap with target