# Used for troubleshooting
# su - msf -c "echo no | msfconsole -qx 'db_disconnect --clear; exit'"
su - msf -c "msfdb init --component database"
msfconsole -x "db_connect msf@msf"