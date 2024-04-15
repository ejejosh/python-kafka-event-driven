#!/bin/bash

docker login
docker build --tag ejejosh/order:v1.0.0 . -f Dockerfile
docker push ejejosh/order:v1.0.0 