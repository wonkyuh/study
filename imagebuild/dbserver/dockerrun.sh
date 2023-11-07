#!/bin/sh

docker run -d --name dbserver -p 3306:3306 -e MARIADB_ROOT_PASSWORD=qwer -e MARIADB_DATABASE=sample mariadb:latest

