# Docker - Nmap (Alpine)

A Dockerized version of the tool Nmap that is small and works on Raspberry pi

**Recommended:** Local build is recommended for Raspberry Pi devices because the Docker daemon will automatically pull down the alpine image that matches the host architecture

## Running with Docker (Local build)

```
docker build -t nmap-small .
```

Build the container (locally)

```
docker run -it nmap-small <arguments> <target>
```

Run nmap with arguments

## Running with Docker (Docker Hub)

```
docker run -it sneakerhax/nmap-small <arguments> <targets>
```

Start image pulled from Docker Hub and run Nmap with target

## DockerSlim

```
docker-slim build --target nmap:latest --http-probe=false --exec "nmap --script=http-title scanme.nmap.org"
```
command to build a smaller image with DockerSlim from already built nmap image (will generate nmap.slim image)
