# Shodan 

A Dockerized version of the Shodan cli

## Building the image

```docker build --build-arg shodan_api_key=$shodan_api_key -t shodan_cli .```

Requires the Shodan api key. This can be passed directly or through an environment variable

## Running the container

```docker run -it shodan_cli <arguments>```

## Usage examples

```docker run -it -v $(pwd):/tmp shodan download /tmp/shodan org:<org_name>```

Download the results of a query and use a volume to persist the data in your host

```docker run -it -v $(pwd):/tmp shodan parse --fields hostnames /tmp/shodan.json.gz```

Extract hostname field using the parse function from shodan json file in host (pipe to `grep "\S"` to remove blank lines)

```docker run -it -v $(pwd):/tmp shodan parse --fields hostnames -f port:80 /tmp/shodan.json.gz | grep "\S"```

Extract hostnames that have port 80 open using the parse function from shodan json file in host and remove blank lines
