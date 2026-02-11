#!/bin/bash

echo "Subindo containers..."
docker compose down
docker compose up --build -d

echo "Containers ativos:"
docker ps
