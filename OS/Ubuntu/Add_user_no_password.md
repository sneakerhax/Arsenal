# Add a user with no password

For use with automation

```
adduser --disabled-password --gecos "" <user>
```

Add a user with no password

```
su - <user>
```

Change to user after logging in

```
passwd <user>
```

Set password (requires root)

```
adduser <user> sudo
```

Optionally add them to the sudo group (requires root)
