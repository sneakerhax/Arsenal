# Docker

Useful commands for running Docker

## Remote

```docker context ls```

List all docker contexts (api endpoints)

```docker -H <host>:<port> info```

Connect to a remote docker api and run info command (requires protocol e.g. tcp:// ssh://)

*Default port is 2375 un-encrypted or 2376 for encrypted communication with the daemon*

```curl -s --unix-socket /var/run/docker.sock http://localhost/version | jq ".ApiVersion"```

Using curl to connect to the Unix socket and pulling the api version

## Images

```docker pull <image_name>```

Pull down an image

```docker images```

List all images (Includes built images)

```docker image build -t <image_name> <location of Dockerfile>```

Building/Updating an image

```docker image history <image_name>```

List the image change history

```docker image inspect <image_name>```

Inspect the image configuration

## Containers

```docker container ps -a```

List all running containers

```docker container ls -a```

List all stopped containers

```docker container stats```

List active stats of running containers

```docker container port <container_name>```

List port mapping in container

```docker container run -t -d <image>```

Create persistent container

```docker container logs <name/id>```

Check the logs of a persistent container (add -f to continue watching)

```docker container run -it <image_name> <argument>```

Start a container that has an ENTRYPOINT and accepts arguments

```docker container exec -it <container_name> <command_name>```

Run command inside of container eg. /bin/bash (must have persistent container)

## Cleanup

```docker rmi <image_name>```

Destroy image

```docker rm <container_name>```

Destroy container

```docker rm -f $(docker ps -a -q)```

Delete all stopped containers (This may be required before removing all dangling images)

```docker rmi -f $(docker images -f "dangling=true" -q)```

Remove all dangling images

## Networking

```docker network ls```

List all docker networks

```docker network inspect <network_name>```

Inspect the details of a network

```docker network create <network_name>```

Create new docker network (default driver is bridge)

```docker network connect/disconnect <network_name> <container_name>```

Connect/disconnect a container from a network

## Volumes

```docker container run -v <name>:<container_path_location> <container_name>```

Run container with named volume that points to a location in the container (Used for persistent data)
