# NSE script searching

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
