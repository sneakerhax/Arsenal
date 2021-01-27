# Kubernetes

## Deploy

```kubectl create deployment <deployment_name> --image=<image_name>```

Create deployment

```kubectl scale deployment/<deployment_name> --replicas 5```

Scaling to 5 replicas

```kubectl expose deployment/<deployment_name> --port 8080```

Expose port inside Kubenetes cluster

## Monitor

```kubectl get all```

List all Kubernetes services and resources

## Cleanup

```kubectl delete deployment <deployment_name>```

Delete deployment
