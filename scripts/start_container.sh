#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull lokeshns/demo-django-app

# Run the Docker image as a container
docker run -d -p 9000:9000 lokeshns/demo-django-app