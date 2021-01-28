# Kubernetes

## Create

```kubectl create deployment <deployment_name> --image=<image_name>```

Create deployment

## Apply

```kubectl apply -f <file_name>.yml --dry-run```

Shows output for the deployment without actually running

## Scale

```kubectl scale deployment/<deployment_name> --replicas 5```

Scaling to 5 replicas

## Expose

```kubectl expose deployment/<deployment_name> --port 8080```

Expose port inside Kubenetes cluster

```kubectl expose deployment/<deployment_name> --port 8080 --name <name> --type NodePort```

Expose port outside cluster (Used for Docker Desktop)

## Get

```kubectl get all```

List all Kubernetes services and resources

```kubectl get services```

List deployed services

```kubectl get namespaces```

List all namespaces

## Explain

```kubectl explain services.spec```

List information about services.spec (yaml spec)

## Delete

```kubectl delete deployment <deployment_name>```

Delete deployment
