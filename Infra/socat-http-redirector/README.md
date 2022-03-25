# Socat HTTP Redirector

A Dockerized Socat HTTP redirector

## Build image

```
docker build -t socat-http-redirector .
```

First replace <ip_address> with the address to redirect traffic


## Running the container

```
docker run -d -p 80:80 socat-http-redirector
```
