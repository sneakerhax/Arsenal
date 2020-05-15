# Docker - Nmap (Kali Linux)

A Dockerized version of Nmap

## Building the image

```docker build -t nmap .```

## Running the container

```docker run -it nmap <target>```

Run nmap (current build tests for port 80. Modify ENTRYPOINT in Dockerfile to change)
