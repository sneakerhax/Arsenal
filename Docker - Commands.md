# Docker - Commands

### Images

```docker pull <image_name>```

Pull down an image

```docker images```

List all images (Includes built images)

```docker build -t <image_name> <location of Dockerfile>```

Building/Updating an image

### Containers

```docker ps -a```

List all containers

```docker run -t -d <image>```

Create persistent container

```docker run -it <image_name> <argument>```

Start a container that has an ENTRYPOINT and accepts arguments

```docker exec -it <container_name> <command_name>```

Run command inside of container eg. /bin/bash (must have persistent container)

### Cleanup

```docker rmi <image_name>```

Destroy image

```docker rm <container_name>```

Destroy container

```docker rmi -f $(docker images -f "dangling=true" -q)```

Remove all dangling images

```docker rm $(docker ps -a -q)```

Delete all stopped containers



