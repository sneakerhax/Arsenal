# C2Concealer

A Dockerized version of the tool C2Concealer by Chris Truncer

## Building the image

```
docker build -t c2concealer .
```

## Running the container

```
docker container run -v <location_of_cobaltstrike>:/usr/share/cobaltstrike/ -it c2concealer
```
