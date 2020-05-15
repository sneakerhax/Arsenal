# C2Concealer

A dockerized version of Chris Truncers C2Concealer

## Building the image

```docker build -t c2concealer .```

## Running the container

```docker container run -v <location_of_cobaltstrike>:/usr/share/cobaltstrike/ -it c2concealer```
