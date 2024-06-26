# Kali Linux install Chrome

**Description:** This entry described how to install Chrome on Kali Linux

**Requirements:** wget

## Installing Google Chrome

```
wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub
```

Download the package public key

```
gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub
```

Make Chrome keyring

```
echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
```

Set the package repository for Google Chrome

```
sudo apt-get update 
sudo apt-get install google-chrome-stable
```

Install Chrome package

* Currently the instructions work as stated in the AskUbuntu article below
  
## References

* [AskUbuntu - How to install Google Chrome ](https://askubuntu.com/questions/510056/how-to-install-google-chrome)
