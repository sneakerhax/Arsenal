# Port scanning using Azure Container Instance

**Description:** This entry describes how to use the Azure container service to run port scans

**Provider:** Azure

**Service:** Container Service

## Logging into Azure (Creating context)

```docker login azure```

Login into Azure

```docker context create aci <context_name>```

Create a new ACI context using the Azure container instance service

## Running your scans

```docker --context <context_name> run -d --name <container_name>  sneakerhax/nmap:latest nmap <args> <target>```

Run an nmap scan using an Azure container instance

```docker --context <context_name> ps -a```

Check the status of the scan

```az container list -o table```

Check the status of the scan using Azure cli


```docker logs <container_name>```

Get the results using docker logs

## References
* https://www.docker.com/blog/how-to-deploy-containers-to-azure-aci-using-docker-cli-and-compose/
* https://azure.microsoft.com/en-us/services/container-instances/
* https://docs.microsoft.com/en-us/azure/container-instances/



