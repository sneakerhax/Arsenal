# Ultra Recon

A tool for running all your recon tools in Docker without remembering Docker commands

This tool is essentially a wrapper for Docker used to run offensive security tools. The tool itself is very small because all it needs to run is one Python file (ultra_recon.py) and the Dockerfiles needed to build the tool images (some tools also contain files that will be added to the image). A wide variety of tools can be added with just a Dockerfile to build the image and a working ```client.containers.run``` configuration. This tool can be made even smaller if all tools are added to an accessible Docker registry such as hub.docker.com

[![Python 3.7](https://img.shields.io/badge/python-3.7-FADA5E.svg?logo=python)](https://www.python.org/) 
[![Docker](https://img.shields.io/badge/docker-required-0db7ed.svg?logo=docker)](https://www.docker.com/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/) [![License](https://img.shields.io/badge/license-GPL3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Twitter](https://img.shields.io/badge/twitter-sneakerhax-38A1F3?logo=twitter)](https://twitter.com/sneakerhax) [![Discord](https://img.shields.io/badge/discord-sneakerhax-7289DA?logo=discord)](https://discordapp.com/invite/wpxpYM3)

![alt text](.img/Ultra_Sun_Ultra_Moon_Ultra_Recon_Squad.png)

## Installation

Install Docker on your local system:
* <https://docs.docker.com/get-docker/>

Install Docker SDK for Python:

```pip3 install -r requirements.txt```

Keys should be added to config.conf (Example for Censys):
```
[censys.io]
censys_API_ID = <censys_API_ID>
censys_secret = <censys_secret>
```

## Usage

```python3 ultra_recon -n <name_of_target> -t <target> -i <docker_image_name>```

## Available Options
```
--name            Name of target (this will become the output folder name)
--target          Target the tool will run on
--image           The name of the image that will run
```

## Example Usage
```
$ Ultra-Recon % python3 ultra_recon.py -n sample -t scanme.nmap.org -i nmap
    __  ______                ____
   / / / / / /__________ _   / __ \___  _________  ____
  / / / / / __/ ___/ __ `/  / /_/ / _ \/ ___/ __ \/ __ \
 / /_/ / / /_/ /  / /_/ /  / _, _/  __/ /__/ /_/ / / / /
 \____/_/\__/_/   \__,_/  /_/ |_|\___/\___/\____/_/ /_/

	 by sneakerhax...

[+] Building image nmap
[+] Starting container nmap
[+] writing output to output/sample/nmap.txt
```

## Current images

* Nmap
* PyDNSRecon (Requires Censys API ID + Secret)

## References

* <https://docker-py.readthedocs.io/en/stable/>
