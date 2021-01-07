# Docker-Compose - Commands

## Starting

```docker-compose up```

Running yaml file build (yaml file must be called docker-compose.yml or specified)

```docker-compose build```

Rebuild images created during the build process

## Stopping

```docker-compose down```

Stopping all running services

```docker-compose down -v```

Stops all running services and deletes volumes

```docker-compose --rmi all```

Delete all images created during the build
