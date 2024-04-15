#!/bin/bash

docker login
docker build --tag ejejosh/transaction:v1.0.0 . -f Dockerfile
docker push ejejosh/transaction:v1.0.0 