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

# log output to file
exec &> $HOME/install.out

# Update all packages

export DEBIAN_FRONTEND=noninteractive
apt update && apt upgrade -y

# install docker

apt-get remove -y docker docker-engine docker.io containerd runc
apt-get update
apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
mkdir -p /etc/apt/keyrings
rm -f /etc/apt/keyrings/docker.gpg
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Apt installs
apt install mosh make nmap ncrack libpcap-dev gcc python3-pip python3-venv -y

# Add recon user

useradd -m -s /bin/bash recon
usermod -aG sudo,docker recon

# Setup directories
su - recon -c "mkdir -p /home/recon/Data /home/recon/Repos /home/recon/Wordlists /home/recon/Scripts"

# Add Scripts

su - recon <<'EOF'
echo "hostnamectl set-hostname \$1" > /home/recon/Scripts/set-hostname.sh
echo "exec bash" >> /home/recon/Scripts/set-hostname.sh
EOF

# Install go

wget https://go.dev/dl/go1.26.6.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.26.6.linux-amd64.tar.gz
echo export PATH=$PATH:/usr/local/go/bin:go/bin >> ~/.profile
echo export PATH=$PATH:/usr/local/go/bin:go/bin >> /home/recon/.profile
source ~/.profile

# Install docker recon tools

su - recon <<'EOF'
docker pull sneakerhax/wordlists
docker run -d -v /home/recon/Wordlists:/wordlists sneakerhax/wordlists
EOF

# Install repos

su - recon <<'EOF'
git clone https://github.com/trickest/resolvers /home/recon/Repos/resolvers
git clone https://github.com/sneakerhax/Containers.git /home/recon/Repos/Containers
git clone https://github.com/sneakerhax/Tacticontainer /home/recon/Repos/Tacticontainer
git clone https://github.com/blechschmidt/massdns /home/recon/Repos/massdns && cd /home/recon/Repos/massdns && make
EOF

# Copy massdns to system path
if [ -f /home/recon/Repos/massdns/bin/massdns ]; then
    cp /home/recon/Repos/massdns/bin/massdns /usr/bin/
else
    echo "massdns build failed, skipping install to /usr/bin" >&2
fi

# Install go tools

su - recon <<'EOF'
export CGO_ENABLED=1
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
EOF
# echo source ~/.bashrc >> ~/.profile
# source ~/.profile

# Install brew

# pre-create and hand over the install dir so the installer doesn't need sudo
mkdir -p /home/linuxbrew/.linuxbrew
chown recon:recon /home/linuxbrew/.linuxbrew

su - recon -c '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'

su - recon <<'EOF'
echo >> /home/recon/.bashrc
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)"' >> /home/recon/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)"
brew install claude-cli copilot-cli
EOF
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Ubuntu recon)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Ubuntu recon installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://help.ubuntu.com/
