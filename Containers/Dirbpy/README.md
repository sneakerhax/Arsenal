# Dirbpy

A Dockerized version of Dirbpy by marcolivierbouch

## Running with Docker (Local Build)

```
docker build -t dirbpy .
```

Building the image (locally)

```
docker run -it dirbpy <arguments>
```

Running the Docker container with arguments

## Running with Docker (Docker Hub)

```
docker run -it sneakerhax/dirbpy <arguments>
```

Start container with the image pulled from Docker Hub and run dirbpy with arguments

```
docker run -it sneakerhax/dirbpy -u http://<ip_address>/ -o <remote wordlist>
```

Run a wordlist on the specified target using remote wordlist (for wordlists hosted on Github you must use raw format)
