# Creating a StackScript to install Docker

**Description:** This entry describes how to setup a script to install Docker engine on virtual machines

**Provider:** Linode

**Service:** StackScript

## Setting up a Docker install StackScript

1. Navigate to StackScripts in the navigation panel on the left side then choose **Create StackScript**

2. Add a description in the **Description** Field

3. Choose **Debian 13** from the **Target Images** dropdown

4. Add the below StackScript to the **Script** field

5. Optionally add a revision note to the **Revision Note** field

```
#!/bin/bash

# log output to file
exec &> $HOME/install.out

# Enable noninteractive in debconf for unnattended install 
export DEBIAN_FRONTEND=noninteractive

apt remove -y $(dpkg --get-selections docker.io docker-compose docker-doc docker-buildx podman-docker containerd runc | cut -f1)

# Add Docker's official GPG key:
apt update
apt install -y ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

# Update packages after adding apt sources
apt update

# Install Docker packages
apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Docker engine)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Docker engine installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://www.debian.org/distrib/
* https://docs.docker.com/engine/install/debian/
