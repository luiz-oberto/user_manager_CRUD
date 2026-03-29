#!/bin/bash

set -e

echo "========================================"
echo "  Iniciando setup do ambiente Docker"
echo "========================================"

# Atualizar sistema
echo "  Atualizando pacotes..."
sudo apt-get update

# 1. Pré-requisitos
echo "  Instalando dependências básicas..."
sudo apt-get install -y ca-certificates curl gnupg

# 2. Adicionar chave GPG do Docker
echo "  Adicionando chave GPG do Docker..."
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 3. Adicionar repositório Docker
echo "  Adicionando repositório do Docker..."

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Atualizar índice e instalar Docker + Compose
echo "  Instalando Docker e Docker Compose..."

sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 5. Habilitar e iniciar Docker
echo "  Ativando Docker..."
sudo systemctl enable docker
sudo systemctl start docker

# 6. Adicionar usuário ao grupo docker
echo "  Adicionando usuário ao grupo docker..."
sudo usermod -aG docker $USER

echo "========================================"
echo "  Docker instalado com sucesso!"
echo "========================================"

# 7. Teste básico
echo "  Testando Docker..."
sudo docker --version
sudo docker compose version

echo ""
echo "  IMPORTANTE:"
echo "Para usar docker sem sudo, faça logout/login ou rode:"
echo "newgrp docker"
echo ""

echo "Ambiente pronto para uso!"