# Creating a StackScript to install Ubuntu for recon

**Description:** This entry describes how to setup a script to Ubuntu for recon on virtual machines

**Provider:** Linode

**Service:** StackScript

## Setting up a Ubuntu recon install StackScript

1. Navigate to StackScripts in the navigation panel on the left side then choose **Create StackScript**

2. Add a description in the **Description** Field

3. Choose **Ubuntu 22.04 LTS** from the **Target Images** dropdown

4. Add the below StackScript to the **Script** field

5. Optionally add a revision note to the **Revision Note** field

```
#!/bin/bash

# Update all packages
export DEBIAN_FRONTEND=noninteractive
sudo apt update && apt upgrade -y

# install docker
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo rm /etc/apt/keyrings/docker.gpg
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Apt installs
apt install mosh make nmap ncrack -y

# Setup directories
mkdir $HOME/Data $HOME/Repos $HOME/Wordlists $HOME/Scripts

# Add Scripts
echo "hostnamectl set-hostname \$1" > $HOME/Scripts/set-hostname.sh
echo "exec bash" >> $HOME/Scripts/set-hostname.sh

# Install go
apt install golang-go -y
echo export GOPATH=$HOME/go >> ~/.profile
source ~/.profile
echo export PATH=$PATH:$GOPATH/bin >> ~/.profile

# Install docker recon tools

# docker pull projectdiscovery/subfinder

# docker pull projectdiscovery/shuffledns
docker pull sneakerhax/wordlists
docker run -d -v $HOME/Wordlists:/wordlists sneakerhax/wordlists

# Install repos
git clone https://github.com/trickest/resolvers $HOME/Repos/resolvers
git clone https://github.com/sneakerhax/Arsenal.git $HOME/Repos/Arsenal
git clone https://github.com/blechschmidt/massdns $HOME/Repos/massdns && cd $HOME/Repos/massdns && make && cp $HOME/Repos/massdns/bin/massdns /usr/bin/

# Install go tools
# go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest && echo source ~/.bashrc >> ~/.profile
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Ubuntu recon)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Ubuntu recon installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://help.ubuntu.com/
