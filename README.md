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

Antes de iniciar, certifique-se de ter instalado:

* Docker
* Docker Compose

### 🔹 Instalar Docker (Ubuntu/Debian)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker
```

---

## 📁 Clonando o projeto

```bash
git clone https://github.com/seu-usuario/user_manager.git
cd user_manager
```

---

## 🔐 Configuração do ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o arquivo `.env`:

```bash
nano .env
```

Exemplo:

```env
# DATABASE CONFIG
DB_HOST=db
DB_NAME=userManager
DB_USER=nevat
DB_PASSWORD=senha_segura_aqui

# JWT CONFIG
SECRET_KEY=sua_chave_super_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🐳 Subindo a aplicação com Docker

```bash
docker compose up --build -d
```

### 🔍 Ver containers ativos:

```bash
docker ps
```

---

## 🌐 Acessando a API

Abra no navegador:

```
http://localhost:8000/docs
```

Interface interativa do Swagger será exibida.

---

## 🔐 Autenticação

### 🔹 Obter token

Endpoint:

```
POST /token
```

Tipo de Body: `x-www-form-urlencoded`

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

### 🔹 Usar token

Adicionar no header:

```
Authorization: Bearer TOKEN_JWT
```

---

## 🧪 Testando a API

### 🔹 Criar usuário (apenas superuser)

```
POST /users
```

---

### 🔹 Listar usuários (apenas superuser)

```
GET /users
```

---

### 🔹 Buscar usuário por ID

```
GET /users/{id}
```

---

### 🔹 Atualizar usuário

```
PUT /users/{id}
```

---

### 🔹 Deletar usuário

```
DELETE /users/{id}
```

---

## 🛂 Controle de permissões

| Tipo de usuário | Permissões                               |
| --------------- | ---------------------------------------- |
| Usuário comum   | Ver próprio perfil                       |
| Superusuário    | Criar, listar, editar e remover usuários |

---

## 💾 Persistência de dados

O banco de dados utiliza volume Docker:

```
postgres_data
```

Isso garante que os dados não sejam perdidos ao reiniciar os containers.

---

## 🔄 Reiniciar a aplicação

```bash
docker compose down
docker compose up -d
```

---

## 🧹 Resetar completamente o ambiente

```bash
docker compose down -v
docker compose up --build
```

⚠️ Isso apagará todos os dados do banco.

---

## 🧠 Estrutura do projeto

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

## 📌 Observações

* O banco de dados é inicializado automaticamente na primeira execução
* O token JWT possui expiração configurável
* A aplicação segue arquitetura stateless

---

## 🚀 Próximos passos

* Implementação de refresh token
* Deploy em VPS com Nginx
* HTTPS com Let's Encrypt
* Frontend web

---

## 👨‍💻 Autor
Desenvolvido por Luiz Oberto Matos Raiol

Engenheiro/Analista de TI com foco em Backend e Segurança da Informação.  
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
