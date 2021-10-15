# Shodan 

A Dockerized version of the Shodan cli

## Building the image

```docker build --build-arg shodan_api_key=$shodan_api_key -t shodan_cli .```

Requires the Shodan api key. This can be passed directly or through an environment variable

## Running the container

```docker run -it shodan_cli <arguments>```

## Usage examples

```docker run -it -v $(pwd):/tmp shodan download /tmp/<org>_shodan org:<org_name>```

Download the results of a query and use a volume to persist the data in your host
