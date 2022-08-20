# Ngrok

```
docker run -it -e NGROK_AUTHTOKEN=<ngrok_auth_token> ngrok/ngrok http host.docker.internal:8081 --region=us --hostname=hostname -auth="user:passwordpassword"
```

Listen on the host machine port 8081