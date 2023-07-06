#! /bin/sh

docker build -t tcp_server -f docker/server/Dockerfile .
docker build -t receive_message -f docker/receive_message/Dockerfile .

# docker-compose build --build-arg DATA_TO_SEND="26+32"
# docker-compose up
