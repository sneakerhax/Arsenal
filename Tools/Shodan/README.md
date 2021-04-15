# Shodan 

A Dockerized version of the Shodan cli

## Building the image

```docker build --build-arg shodan_api_key=$shodan_api_key -t shodan_cli .```

Requires the Shodan api key. This can be passed directly or through an environment variable shown above

## Running the container

```docker run -it shodan_cli <arguments>```
