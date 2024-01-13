#!/bin/bash

container=$(podman ps --noheading | grep expense-bot | awk '{print$1}')
sudo podman stop $container
sudo podman rm $container
sudo podman run -d --name expense-bot --restart always quay.io/ksemele/expense-bot:0.1.0
