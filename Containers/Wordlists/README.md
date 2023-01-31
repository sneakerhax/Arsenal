# Docker - Wordlists

A Dockerized Wordlists downloader

## Building the image (Local build)

```
docker build -t wordlists .
```

## Running the container

```
docker run -it -v $(pwd):/wordlists wordlists
```

Running wordlists and adding all files to your current directory
