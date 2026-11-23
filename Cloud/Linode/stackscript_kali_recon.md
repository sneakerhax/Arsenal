# Creating a StackScript to install Kali for recon

**Description:** This entry describes how to set up a Linode Stackscript on a Kali Linux virtual machine to install recon tools.

**Provider:** Linode

**Service:** StackScript

## Setting up a Kali recon install StackScript

1. Navigate to StackScripts in the navigation panel on the left side then choose **Create StackScript**

2. Add a description in the **Description** Field

3. Choose **Kali Linux** from the **Target Images** dropdown

4. Add the below StackScript to the **Script** field

5. Optionally add a revision note to the **Revision Note** field

```
#!/bin/bash

# Update all packages
export DEBIAN_FRONTEND=noninteractive
apt update && apt upgrade -y

# Apt installs
apt install mosh nmap ncrack docker.io golang-go libpcap-dev massdns -y

# Add gopath
echo export GOPATH=$HOME/go >> ~/.zshrc
echo export PATH=$PATH:$GOPATH/bin >> ~/.zshrc
source ~/.zshrc

# Setup directories
mkdir -p $HOME/Data $HOME/Repos $HOME/Wordlists $HOME/Scripts

# Add Scripts
echo "hostnamectl set-hostname \$1" > $HOME/Scripts/set-hostname.sh
echo "exec bash" >> $HOME/Scripts/set-hostname.sh
chmod +x $HOME/Scripts/set-hostname.sh

# Install docker recon tools
systemctl enable --now docker
until docker info >/dev/null 2>&1; do sleep 1; done
docker pull sneakerhax/wordlists:latest
docker run -d -v $HOME/Wordlists:/wordlists sneakerhax/wordlists

# Install repos
git clone https://github.com/trickest/resolvers $HOME/Repos/resolvers || echo "failed to clone resolvers"
git clone https://github.com/sneakerhax/Arsenal.git $HOME/Repos/Arsenal || echo "failed to clone Arsenal"
git clone https://github.com/sneakerhax/Containers.git $HOME/Repos/Containers || echo "failed to clone Containers"
git clone https://github.com/sneakerhax/Ultra-Recon $HOME/Repos/Ultra-Recon || echo "failed to clone Ultra-Recon"

# Install recon tools
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest || echo "failed to install pdtm"
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Kali recon)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Kali recon installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://www.kali.org/docs/
