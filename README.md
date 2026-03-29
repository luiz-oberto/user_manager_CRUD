# 🚀 User Manager API

API REST desenvolvida em **FastAPI** para gerenciamento de usuários, com autenticação via **OAuth2 + JWT**, controle de permissões e persistência em **PostgreSQL**.

---

## 📌 Funcionalidades

* ✅ CRUD completo de usuários
* 🔐 Autenticação com OAuth2 (Password Flow)
* 🔑 Autorização com JWT
* 🛂 Controle de permissões (usuário / superusuário)
* 🐳 Containerização com Docker
* 💾 Persistência de dados com volume Docker

---

## 🏗️ Tecnologias utilizadas

* Python 3.11+
* FastAPI
* PostgreSQL 16
* Uvicorn
* Docker / Docker Compose
* JWT (python-jose)
* Passlib / Werkzeug

---

## ⚙️ Pré-requisitos

* Sistema baseado em Linux (Ubuntu recomendado)
* Git

---

## 📁 Clonando o projeto

```bash
git clone https://github.com/seu-usuario/user_manager.git
cd user_manager
```

---

# 🐳 🔧 Configuração automática do Docker (RECOMENDADO)

Este projeto inclui um script para instalar automaticamente o Docker e o Docker Compose Plugin.

### ▶️ Executar o script

```bash
chmod +x setup_server.sh
./setup_server.sh
```

---

### ⚠️ Após execução

Execute:

```bash
newgrp docker
```

Isso permite usar Docker sem `sudo`.

---

### 🔍 Validar instalação

```bash
docker --version
docker compose version
```

---

# 🔐 Configuração do ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o arquivo:

```bash
nano .env
```

Exemplo:

```env
# DATABASE CONFIG
DB_HOST=db
DB_NAME=userManager
DB_USER=YOUR_USER
DB_PASSWORD=senha_segura_aqui

# JWT CONFIG
SECRET_KEY=sua_chave_super_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 🐳 Subindo a aplicação

```bash
docker compose up --build -d
```

---

### 🔍 Ver containers ativos

```bash
docker ps
```

---

# 🌐 Acessando a API

Abra no navegador:

```
http://localhost:8000/docs
```

---

# 🔐 Autenticação

## 🔹 Obter token

Endpoint:

```
POST /token
```

Body: `x-www-form-urlencoded`

```
username=email@exemplo.com
password=senha
```

Resposta:

```json
{
  "access_token": "TOKEN_JWT",
  "token_type": "bearer"
}
```

---

## 🔹 Usar token

Header:

```
Authorization: Bearer TOKEN_JWT
```

---

# 🧪 Testando a API

### Criar usuário (superuser)

```
POST /users
```

---

### Listar usuários (superuser)

```
GET /users
```

---

### Buscar usuário

```
GET /users/{id}
```

---

### Atualizar usuário

```
PUT /users/{id}
```

---

### Deletar usuário

```
DELETE /users/{id}
```

---

# 🛂 Controle de permissões

| Tipo          | Permissões                |
| ------------- | ------------------------- |
| Usuário comum | Visualizar próprio perfil |
| Superusuário  | Gerenciar usuários        |

---

# 💾 Persistência de dados

A aplicação utiliza volume Docker:

```
postgres_data
```

Os dados permanecem mesmo após reinicialização.

---

# 🔄 Reiniciar aplicação

```bash
docker compose down
docker compose up -d
```

---

# 🧹 Reset completo (apaga banco)

```bash
docker compose down -v
docker compose up --build
```

---

# 🧠 Estrutura do projeto

```
app/
├── routes/
├── services/
├── schemas/
├── database.py
├── main.py

docker/
└── db_init/
    └── init.sql
```

---

# 📌 Observações

* O banco é inicializado automaticamente na primeira execução
* JWT possui expiração configurável
* Arquitetura stateless

---

# 🚀 Próximos passos

* Refresh token
* Deploy com Nginx
* HTTPS
* Frontend

---

## 👨‍💻 Autor
Desenvolvido por Luiz Oberto Matos Raiol

Analista de TI com foco em Backend e Segurança da Informação.  
Experiência em desenvolvimento de APIs, automação e infraestrutura.

Este projeto demonstra:

- Desenvolvimento de API REST com FastAPI  
- Implementação de autenticação OAuth2 + JWT  
- Controle de acesso baseado em permissões  
- Containerização com Docker  
- Integração com PostgreSQL  

🔗 LinkedIn: https://www.linkedin.com/in/luiz-oberto-matos-raiol-217038283/

🔗 GitHub: https://github.com/luiz-oberto

---
