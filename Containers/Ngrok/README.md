# Ngrok

```
docker run -it -e NGROK_AUTHTOKEN=<ngrok_auth_token> ngrok/ngrok http host.docker.internal:8080 --region=us --hostname=hostname --basic-auth="user:password"
```

Create an http Ngrok tunnel that exposes your host 8080 (For local testing on Docker desktop for MacOS and Windows)

```
docker run --net=host -it -e NGROK_AUTHTOKEN=<ngrok_auth_token> ngrok/ngrok http 8080 --region=us --basic-auth="user:password" 
```

Create an http Ngrok tunnel that exposes your host 8080 (For none Docker Desktop such as cloud virtual machine)

## References
* [Using ngrok with Docker](https://ngrok.com/docs/using-ngrok-with/docker/)
