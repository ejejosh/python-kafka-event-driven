#!/bin/bash

docker login
docker build --tag ejejosh/notification:v1.0.0 . -f Dockerfile
docker push ejejosh/notification:v1.0.0 