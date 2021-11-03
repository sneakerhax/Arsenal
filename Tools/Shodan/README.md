# Shodan 

A Dockerized version of the Shodan cli

## Building the image

```
docker build --build-arg shodan_api_key=$shodan_api_key -t shodan_cli .
```

Requires the Shodan api key. This can be passed directly or through an environment variable

## Running the container

```
docker run -it shodan_cli <arguments>
```

## Usage examples

```
docker run -it shodan count org:<org_name>
```

Use the count function to check the number of results for a search query (Used to know how many credits you will use on a search)

```
docker run -it -v $(pwd):/tmp shodan download /tmp/shodan org:<org_name>
```

Download the results of a query and use a volume to persist the data in your host (default is 1000 results)

```
docker run -it -v $(pwd):/tmp shodan download --limit -1 /tmp/shodan org:<org_name>
```

Download the results of a query and use a volume to persist data in your host (Get all results available)

```
docker run -it -v $(pwd):/tmp shodan parse --fields hostnames /tmp/shodan.json.gz
```

Extract hostname field using the parse function from shodan json file in host (pipe to `grep "\S"` to remove blank lines)

```
docker run -it -v $(pwd):/tmp shodan parse --fields hostnames -f port:80 /tmp/shodan.json.gz | grep "\S"
```

Extract hostnames that have port 80 open using the parse function from shodan json file in host and remove blank lines

```
docker run -it -v $(pwd):/tmp shodan parse --no-color --fields ip_str,hostnames,port,org --separator : /tmp/shodan.json.gz > shodan.txt
```

Extract IP, hostnames, ports, and org and separate them by `:` then dump to file (--no-color is to avoid terminal color characters in text file)

```
docker run -it -v $(pwd):/tmp shodan parse --fields ip_str,hostnames,port,org --separator : -f product:"Apache httpd" /tmp/shodan.json.gz
```

Same as previous but find Apache servers (add --no-color for piping to file)

```
docker run -it -v $(pwd):/tmp shodan parse --fields ip_str,hostnames,port,product,version,org --separator : -f product:"Apache httpd" -f version:"2.4.29" /tmp/shodan_all.gz
```

Same as previous but search a particular version (add --no-color for piping to file)


