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

* Sistema operacional Linux (Ubuntu recomendado)
* Git

---

## 📁 Clonando o projeto

```bash
git clone https://github.com/luiz-oberto/user_manager_CRUD.git
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

## ⚙️ Configuração de Variáveis de Ambiente

Este projeto utiliza variáveis de ambiente para configuração da aplicação.

### 📁 1. Criar o arquivo `.env`

Antes de executar o projeto, copie o arquivo de exemplo:

```bash
cp .env.example .env
```

---

### ✏️ 2. Preencher as variáveis

Edite o arquivo `.env` com valores reais:

#### 🔹 Banco de Dados

* `DB_HOST` → Host do banco (em Docker: `db`)
* `DB_NAME` → Nome do banco de dados
* `DB_USER` → Usuário do banco
* `DB_PASSWORD` → Senha do banco

#### 🔹 Autenticação (JWT)

* `SECRET_KEY` → Chave secreta para geração dos tokens (use uma chave forte)
* `ALGORITHM` → Algoritmo de assinatura (ex: `HS256`)
* `ACCESS_TOKEN_EXPIRE_MINUTES` → Tempo de expiração do token

#### 🔹 Usuário Administrador (Bootstrap automático)

* `ADMIN_EMAIL` → Email do superusuário inicial
* `ADMIN_PASSWORD` → Senha do superusuário inicial

> ⚠️ Caso essas variáveis não sejam definidas, a aplicação utilizará valores padrão (somente para desenvolvimento).

---

### 🔐 Gerando uma SECRET_KEY segura

Execute:

```bash
openssl rand -hex 32
```

---

### 🐳 Observação (Docker)

* O serviço da API lê automaticamente o arquivo `.env`
* Certifique-se de que as credenciais do banco (`DB_USER` e `DB_PASSWORD`) estão alinhadas com o `docker-compose.yml`

---

### 🚀 Inicialização

Após configurar o `.env`, execute:

```bash
docker compose up --build
```

A aplicação irá:

1. Subir o banco PostgreSQL
2. Iniciar a API FastAPI
3. Criar automaticamente um superusuário (caso ainda não exista)

---

### 🔍 Acesso à API

* Documentação interativa:
  http://IP_DA_MAQUINA:8000/docs

---

# 🔐 Autenticação

## 🔹 Obter token

Endpoint:

```
POST /token
```

Body: `x-www-form-urlencoded`

```
username=Nome
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
# 🔄 Fluxo de uso da API

1. A aplicação inicia e cria automaticamente um superusuário (caso não exista)
2. O usuário realiza autenticação via `/token`
3. Um token JWT é retornado
4. O token é utilizado para acessar endpoints protegidos
5. O superusuário pode gerenciar usuários no sistema

---

# 🧪 Testando a API
> 🔐 Todos os endpoints protegidos requerem token JWT no header:
>
> Authorization: Bearer <seu_token>
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

### Exemplo de login via curl

```bash
curl -X POST "http://localhost:8000/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=api_admin@local&password=suaSenha"
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
├── utils/
├── database.py
├── main.py

docker/
└── db_init/
    └── init.sql
```
---
# 🔒 Segurança

- Senhas armazenadas com hash (bcrypt)
- Autenticação baseada em JWT
- Controle de acesso por nível de usuário
- Variáveis sensíveis protegidas via `.env`
- `.env` não versionado
---

# 📌 Observações

* O banco é inicializado automaticamente na primeira execução
* JWT possui expiração configurável
* Arquitetura stateless

---

# 🚀 Próximos passos

* Implementação de refresh token
* Deploy com Nginx e reverse proxy
* Configuração de HTTPS (TLS)
* Integração com frontend
* Controle de roles mais granular (RBAC)

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
