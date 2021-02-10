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

List all Kubernetes services and resources

```kubectl get services```

List deployed services

```kubectl get namespaces```

List namespaces in your curent context

```kubectl get all --all-namespaces```

List all namespaces

## Explain

```kubectl explain services.spec```

List information about services.spec (yaml spec)

## Delete

```kubectl delete deployment <deployment_name>```

Delete deployment

## Attacking

```mount | grep kube```

Searching for the serviceaccount folder (Default: /run/secrets/kubernetes.io/serviceaccount)

Important files:
* ca.crt
* namespace
* token (service account token)

```
env

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=nginx-6799fc88d8-2pgh2
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
NGINX_VERSION=1.19.6
NJS_VERSION=0.5.0
PKG_RELEASE=1~buster
HOME=/root

```

Search environment variables for api endpoints

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

Downloading a copy of [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (chmod u+x before running)

```
alias kubectl="<path_to_kubectl> --token=`cat /run/secrets/kubernetes.io/serviceaccount/token` --certificate-authority=/run/secrets/kubernetes.io/serviceaccount/ca.crt -n `cat /run/secrets/kubernetes.io/serviceaccount/namespace` --server=https://<api_server_ip>:<api_server_port>"
```

Setup kubectl command with discovered credentials from serviceaccount folder




