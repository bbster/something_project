#!/usr/bin/env bash

container_name=someapi_postgresql
docker rm -f $(docker ps -a | grep $container_name | awk "{print \$1}" )
docker run -itd -p 55432:5432 --name $container_name -e POSTGRES_PASSWORD=password --restart unless-stopped postgres:13