# Creating a StackScript to install Docker

**Description:** This entry describes how to setup a script to install Docker engine on virtual machines

**Provider:** Linode

**Service:** StackScript

## Setting up a Docker install StackScript

1. Navigate to StackScripts in the navigation panel on the left side then choose **Create StackScript**

2. Add a description in the **Description** Field

3. Choose **Ubuntu 20.04 LTS** from the **Target Images** dropdown

4. Add the below StackScript to the **Script** field

5. Optionally add a revision note to the **Revision Note** field

```
#!/bin/bash
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
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Docker engine)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Docker engine installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://docs.docker.com/engine/install/ubuntu/
