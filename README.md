# expense-bot

## Build Image

```
docker build -t expense-bot:latest .
```

## [WIP] Push Image to registry

```
$ podman login quay.io
$ podman push [hash]|[localhost/expense-bot:0.1.0] docker://quay.io/ksemele/expense-bot:0.1.0
```

## Run bot

### local

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### container

Ensure you have an `.env` file with followed content:
```yaml
ADMINS=12345678,12345677,12345676
BOT_TOKEN=0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
HOST_IP=localhost
```
Then run on Docker
```bash
docker run --name expense-bot --env-file .env -d expense-bot:latest
```
or Podman
```bash
podman run --restart always --name expense-bot --env-file .env -d expense-bot:latest
```
