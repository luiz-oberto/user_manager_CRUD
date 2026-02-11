#!/bin/bash

echo "Atualizando sistema..."
sudo apt update && sudo apt upgrade -y

echo "Instalando Docker..."
sudo apt install -y docker.io docker-compose-plugin

echo "Habilitando Docker..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Adicionando usuário ao grupo docker..."
sudo usermod -aG docker $USER

echo "Docker instalado com sucesso!"
