# Git-Dumper

A Dockerized version of the tool git-dumper by arthaud

## Running with Docker (Local Build)

```
docker build -t git-dumper .
```

Building the image (locally)

```
docker run -it -v git-dumper <arguments>
```

Running the Docker container with arguments

```
docker run -it -v $PWD:/tmp git-dumper <URL> </tmp/scan_name>
```
Running the Docker container and getting the output put in your current directory
