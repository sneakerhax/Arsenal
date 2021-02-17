# Kubernetes

## Remote

```kubectl --kubeconfig ~/.kube/config <command>```

Using a kubeconfig file to access a remote API and run commands

```curl https://kubernetes.site.com:6443/api```

Check for the existance of the kubernetes api secure port

*Other relevant [ports](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md) for interacting with kubernetes*

## Create

```kubectl create deployment <deployment_name> --image=<image_name>```

Create deployment

## Apply

```kubectl apply -f <file_name>.yml --dry-run```

Shows output for the deployment without actually running

```kubectl apply -f <file_name>.yml --server-dry-run```

Shows output for deployment by checking API (If deployment exists it will list changes)

## Diff

```kubectl diff -f <file_name>.yml```

Compare differences between current deployment and yml deployment

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

List all Kubernetes services and resources (Current namespace)

```kubectl get services```

List deployed services

```kubectl get namespaces```

List namespaces in your curent context

```kubectl get all --all-namespaces```

List all namespaces

```kubectl get pods --all-namespaces```

List all pods in all namespaces

```kubectl get pods -n <namespace>```

Get all pods in a namespace

## Describe

```kubectl describe node <node_name>```

Detailed information about a node

## Exec

```kubectl exec -it <pod_name> -- /bin/bash```

Drop into interactive bash shell inside pod

```kubectl exec <pod_name> -- <command>```

Execute single command inside pod

## Explain

```kubectl explain services.spec```

List information about services.spec (yaml spec)

```kubectl explain <type>```

Explain a resource type (e.g. node)

## Delete

```kubectl delete deployment <deployment_name>```

Delete deployment
