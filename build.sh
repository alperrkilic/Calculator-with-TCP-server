#! /bin/sh

docker build -t tcp_server -f docker/server/Dockerfile .
docker build -t receive_message -f docker/receive_message/Dockerfile .


# docker-compose up


# Powershell : $env:DATA_TO_SEND = "20*3" (sending environment variable)
# Command line : set DATA_TO_SEND="36+42" (sending environment variable)