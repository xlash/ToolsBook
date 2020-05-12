# Reading List

This is a list of more in-depth articles than can be worth reading to get a better understanding of some of the underlying technologies used by Containers and how things like Kubernetes work.

# Module 1 - Introduction to Docker

### Brief Container History
https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016

### Series of posts on the history of container engines leading up to Docker
http://www.cybera.ca/news-and-events/tech-radar/contain-your-enthusiasm-part-one-a-history-of-operating-system-containers/ 

http://www.cybera.ca/news-and-events/tech-radar/contain-your-enthusiasm-part-two-jails-zones-openvz-and-lxc/

http://www.cybera.ca/news-and-events/tech-radar/contain-your-enthusiasm-part-three-docker/ 


# Module 2 - Docker Networking

### Post on Linux Bridging
https://www.thegeekstuff.com/2017/06/brctl-bridge/ 

### Posts on Docker MACVLAN
https://web.archive.org/web/20190217173244/https://hicu.be/docker-networking-macvlan-vlan-configuration

https://web.archive.org/web/20190130130707/hicu.be/bridge-vs-macvlan

# Module 3 - Building Docker Images

## Container Storage and Volumes

### Post detailing how Docker union Filesystems and storage drivers work
https://integratedcode.us/2016/08/30/storage-drivers-in-docker-a-deep-dive/ 

### Post on union file systems
https://www.terriblecode.com/blog/how-docker-images-work-union-file-systems-for-dummies/ 

### Post with some opinions on the available Docker storage graphdrivers
https://blog.jessfraz.com/post/the-brutally-honest-guide-to-docker-graphdrivers/ 


# Module 4 - Container Fundamentals

### Series of posts from Ian Lewis on Container runtimes
https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r

https://www.ianlewis.org/en/container-runtimes-part-2-anatomy-low-level-contai

https://www.ianlewis.org/en/container-runtimes-part-3-high-level-runtimes

https://www.ianlewis.org/en/container-runtimes-part-4-kubernetes-container-run   

## Linux Namespaces

### Start of a good series of posts on LWN about Namespaces
https://lwn.net/Articles/531114/ 

### Good Series of Articles on Namespaces
http://ifeanyi.co/posts/linux-namespaces-part-1/

http://ifeanyi.co/posts/linux-namespaces-part-2/ 

http://ifeanyi.co/posts/linux-namespaces-part-3/

http://ifeanyi.co/posts/linux-namespaces-part-4/


### Post specifically focusing on the PID namespace and it's relation to containers
https://hackernoon.com/the-curious-case-of-pid-namespaces-1ce86b6bc900 

### Post from Jessie Frazelle about non-namespaces resources in Linux
https://blog.jessfraz.com/post/two-objects-not-namespaced-linux-kernel/ 

## Linux Capabilities

### This is a good series of posts on capabilities
http://blog.siphos.be/2013/05/capabilities-a-short-intro/

http://blog.siphos.be/2013/05/restricting-and-granting-capabilities/

http://blog.siphos.be/2013/05/overview-of-linux-capabilities-part-1/

http://blog.siphos.be/2013/05/overview-of-linux-capabilities-part-2/

http://blog.siphos.be/2013/05/overview-of-linux-capabilities-part-3/

### This post goes into the slightly obscure topic of "ambient capabilities"
https://s3hh.wordpress.com/2015/07/25/ambient-capabilities/ 

### Toolset used most for poking at capabilities
https://people.redhat.com/sgrubb/libcap-ng/index.html 

### Post from spender of grsecurity fame.  Talks about privesc possibilities from certain capabilities.
https://forums.grsecurity.net/viewtopic.php?f=7&t=2522&sid=c6fbcf62fd5d3472562540a7e608ce4e#p10271 


### Post, which isn't just on capabilities.  It goes into the idea of building your own containers, and as part of that, covers capabilities

https://blog.lizzie.io/linux-containers-in-500-loc.html 

### Post about LXC and capabilities

https://blog.iwakd.de/lxc-cap_sys_admin-jessie 


## CGroups

### Post detailing how Docker uses cgroups

https://shekhargulati.com/2019/01/03/how-docker-uses-cgroups-to-set-resource-limits/ 


# Module 5 - Docker Security

### Post on Docker Authorization plugins

https://blog.aquasec.com/docker-1.10-security-features-part-2-authorization-plug-in

# Module 6 - Docker Swarm

### Docker Swarm Certificate management

https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/

# Module 7 - Introduction to Kubernetes

### Kubernetes the Hard Way - Tutorial on clsuter building

https://github.com/kelseyhightower/kubernetes-the-hard-way

### Post that goes into a lot of detail of how Kubernetes works to create a deployment

https://github.com/jamiehannaford/what-happens-when-k8s 

### Post on What a Kubernetes Pod is

https://www.ianlewis.org/en/what-are-kubernetes-pods-anyway 

### Post on the pause container

https://www.ianlewis.org/en/almighty-pause-container 

## Container Networking

### Good series of posts on Kubernetes networking fundamentals

https://medium.com/google-cloud/understanding-kubernetes-networking-pods-7117dd2872

https://medium.com/google-cloud/understanding-kubernetes-networking-services-f0cb48e4cc82

https://medium.com/google-cloud/understanding-kubernetes-networking-ingress-1bc341c84078 

### Another good set of posts on Container networking setup

https://itnext.io/an-illustrated-guide-to-kubernetes-networking-part-1-d1ede3322727

https://itnext.io/an-illustrated-guide-to-kubernetes-networking-part-2-13fdc6c4e24c

### Implementing your own CNI plugin in Bash

https://www.altoros.com/blog/kubernetes-networking-writing-your-own-simple-cni-plug-in-with-bash/ 

# Module 8 - Kubernetes Security

### Playlist of Kubernetes pentesting/security videos
https://www.youtube.com/playlist?list=PLKDRii1YwXnLmd8ngltnf9Kzvbja3DJWx 

### Post on creating reverse shells from Docker and Kubernetes
https://raesene.github.io/blog/2019/08/09/docker-reverse-shells/

### Post on getting reverse shells on every node in a cluster
https://raesene.github.io/blog/2019/08/10/making-it-rain-shells-in-Kubernetes/

# Bonus Module - Windows Containers

### Windows container Storage
https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-storage

### Windows Container Base Images
https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-base-images 


# Books 

### Free Kubernetes Security book from Aqua

https://info.aquasec.com/kubernetes-security

### Docker in Practice 

https://www.manning.com/books/docker-in-practice-second-edition
