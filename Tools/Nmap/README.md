# Nmap

Nmap is a port scanning tool used for discovery and enumeration of targets

## Installation
* Install [Nmap](https://nmap.org/download.html)
* Install [Nmap with Brew](https://formulae.brew.sh/formula/nmap)

## NSE scripts

NSE (Nmap Scripting Engine) is a collection of scripts that extend Nmap's core capabilites

* [NSE Scripts](https://nmap.org/nsedoc/scripts/)

## NSE script searching

The following functions can be added to your shell configuration file to allow you to search available nse scripts in your terminal

OSX

```
nse(){ find /usr/local/share/nmap/scripts/ -iname "*$1*" | cut -c32- | cut -d'.' -f1;i}
```

Linux

```
nse(){ find /usr/share/nmap/scripts/ -iname *$1* -printf '%P\n';}
```

Setup custom functions for searching nse scripts (Created by hecky)

```
nse search
```

Example usage of custom nse function

## References
* [Nmap](https://nmap.org/) 
* [Nmap Reference Guide](https://nmap.org/book/man.html)

