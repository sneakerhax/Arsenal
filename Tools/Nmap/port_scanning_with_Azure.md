# Port scanning using Azure

## Logging into Azure (Creating context)

```docker login azure```

Login into Azure

```docker context create aci <context_name>```

Create a new ACI context using the Azure container instance service

## Running your scans

```docker --context <context_name> run -d --name <container_name>  sneakerhax/nmap:latest nmap <args> <target>```

Run an nmap scan using an Azure container instance

```docker logs <container_name>```

Get the results using docker logs

## References
* https://www.docker.com/blog/how-to-deploy-containers-to-azure-aci-using-docker-cli-and-compose/



