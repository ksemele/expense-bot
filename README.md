# [WIP]

# Build Image
```
$ sudo podman build -t expense-bot:0.1.0 .
```
# Push Image to registry
```
$ podman login quay.io
$ podman push [hash]|[localhost/expense-bot:0.1.0] docker://quay.io/ksemele/expense-bot:0.1.0
```
# Run bot
```
$ podman login quay.io
$ podman pull quay.io/ksemele/expense-bot
$ podman pull quay.io/ksemele/expense-bot:0.1.0
```