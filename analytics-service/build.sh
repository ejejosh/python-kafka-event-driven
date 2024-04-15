#!/bin/bash

docker login
docker build --tag ejejosh/analytics:v1.0.0 . -f Dockerfile
docker push ejejosh/analytics:v1.0.0 