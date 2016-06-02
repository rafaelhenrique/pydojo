#!/bin/bash
PORT=5432
NAME=postgres_pydojo
VOLUME=$(pwd)/data_postgres
SO=$(uname)
POSTGRES_PASSWORD=123

mkdir -p $VOLUME
docker pull postgres
# docker run -t -i -p $PORT:$PORT --name $NAME -v $VOLUME:/data redis redis-server --appendonly yes --requirepass $REDIS_PASSWORD
docker run -t -i -p $PORT:$PORT --name $NAME -v $VOLUME:/var/lib/postgresql/data -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD postgres
if [ $? -ne 0 ]; then
   docker start $NAME
   CONTAINER_ID=$(docker ps -a -f name=$NAME --format "{{.ID}}")
   docker logs -f $CONTAINER_ID
fi
