# Creating a StackScript to install Metasploit

**Description:** This entry describes how to setup a script to install Metasploit on virtual machines

**Provider:** Linode

**Service:** StackScript

## Setting up a Metasploit install StackScript

1. Navigate to StackScripts in the navigation panel on the left side then choose **Create StackScript**

2. Add a description in the **Description** Field

3. Choose **Ubuntu 20.04 LTS** from the **Target Images** dropdown

4. Add the below StackScript to the **Script** field

5. Optionally add a revision note to the **Revision Note** field

```
#!/bin/bash
apt update && apt upgrade -y
apt install -y curl gnupg nmap
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
useradd -ms /bin/bash msf
su - msf -c "echo no | msfconsole -qx 'db_disconnect --clear; exit'"
su - msf -c "msfdb init --component database"
echo 'msfconsole -x "db_connect msf@msf"' > msfstart.sh
chmod +x msfstart.sh
```

## Using the StackScript on deployment

1. Navigate to StackScripts in the navigation panel on the left side
2. From the list of StackScripts choose the one you want to deploy (In this case Metasploit)
3. Click the 3 dots to the right side of the StackScript listing and choose **Deploy New Linode**
4. Follow the instructions to deploy a virtual machine with Docker engine installed
  
## References
* https://www.linode.com/docs/guides/platform/stackscripts/
* https://docs.rapid7.com/metasploit/installing-the-metasploit-framework/
