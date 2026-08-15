# 🚀 Marketplace Hub API

Uma API REST desenvolvida com **FastAPI** para gerenciamento de produtos, estoque e pedidos de um marketplace.

O objetivo deste projeto é praticar conceitos de arquitetura de software, FastAPI, PostgreSQL, Docker e boas práticas de desenvolvimento Python.

---

# 🎯 Objetivos

- Aprender FastAPI
- Praticar SQLAlchemy 2.0
- Trabalhar com PostgreSQL
- Implementar autenticação JWT
- Utilizar Docker
- Criar testes automatizados
- Documentar APIs
- Aplicar arquitetura em camadas
- Criar um projeto profissional para portfólio

---

# 🛠 Stack

- Python 3.13+
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Docker
- Docker Compose
- Pytest
- Pydantic
- JWT Authentication
- Redis (Opcional)

---



# 📁 Estrutura do Projeto

```
marketplace-hub-api/

app/
│
├── api/
│   ├── routes/
│   └── dependencies/
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── exceptions.py
│
├── database/
│   ├── database.py
│   ├── models/
│   └── migrations/
│
├── repositories/
│
├── services/
│
├── schemas/
│
├── middleware/
│
├── auth/
│
├── tests/
│
├── main.py
│
.env
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---



# 🏗 Arquitetura

```
Cliente

↓

Router

↓

Service

↓

Repository

↓

Database
```

Cada camada possui apenas uma responsabilidade.

---



# 📚 Funcionalidades



## ✅ Usuários

- Cadastro
- Login
- JWT
- Refresh Token
- Alterar senha

---



## ✅ Produtos

- Criar
- Atualizar
- Excluir
- Buscar por ID
- Listagem paginada
- Buscar por nome
- Buscar por SKU

---



## ✅ Categorias

CRUD completo

---



## ✅ Fornecedores

CRUD completo

---



## ✅ Estoque

Adicionar estoque

Remover estoque

Histórico de movimentação

Quantidade disponível

Quantidade reservada

---



## ✅ Pedidos

Criar pedido

Cancelar pedido

Finalizar pedido

Status do pedido

---



## ✅ Dashboard

Produtos sem estoque

Produtos mais vendidos

Pedidos do dia

Faturamento

---



# 🔒 Autenticação

Será utilizado JWT.

Endpoints públicos:

```
POST /login

POST /register
```

Endpoints protegidos:

```
GET /products

POST /products

DELETE /products/{id}
```

---



# 📦 Banco de Dados

Tabelas:

```
users

products

categories

suppliers

inventory

orders

order_items
```

---



# 📖 Endpoints



## Produtos

```
GET /products

GET /products/{id}

POST /products

PUT /products/{id}

DELETE /products/{id}
```

---



## Categorias

```
GET /categories

POST /categories

PUT /categories/{id}

DELETE /categories/{id}
```

---



## Estoque

```
POST /inventory/input

POST /inventory/output

GET /inventory/history
```

---



## Pedidos

```
GET /orders

POST /orders

GET /orders/{id}

PUT /orders/{id}

DELETE /orders/{id}
```

---



# ✅ Validações

Todos os Schemas utilizarão Pydantic.

Exemplo:

- Nome obrigatório
- SKU único
- Preço maior que zero
- Quantidade positiva

---



# 🧪 Testes

Utilizar Pytest.

Testar:

- Login
- Cadastro
- Produtos
- Estoque
- Pedidos

Cobertura mínima:

```
80%
```

---



# 📋 Roadmap



## Etapa 1

- [ ] Configurar projeto
- [ ] Docker
- [ ] PostgreSQL
- [ ] FastAPI
- [ ] SQLAlchemy

---



## Etapa 2

- [ ] Usuários
- [ ] Login
- [ ] JWT
- [ ] Autenticação

---



## Etapa 3

- [ ] Produtos
- [ ] Categorias
- [ ] Fornecedores

---



## Etapa 4

- [ ] Estoque
- [ ] Movimentações

---



## Etapa 5

- [ ] Pedidos

---



## Etapa 6

- [ ] Dashboard

---



## Etapa 7

- [ ] Testes

---



## Etapa 8

- [ ] CI/CD GitHub Actions

---



## Etapa 9

- [ ] Deploy

---



# 📈 Melhorias Futuras

- Redis
- Celery
- Upload de imagens
- S3
- Mercado Livre API
- Shopee API
- Amazon API
- RabbitMQ
- WebSockets
- Cache
- Logs estruturados
- OpenTelemetry
- Prometheus
- Grafana

---



# 🎓 Conceitos praticados

- FastAPI
- Dependency Injection
- SQLAlchemy 2
- Alembic
- Repository Pattern
- Service Layer
- JWT
- Docker
- PostgreSQL
- REST API
- HTTP Status
- Swagger
- OpenAPI
- Testes
- Clean Code
- SOLID

---



# 🏆 Objetivo Final

Criar uma API REST profissional, utilizando boas práticas de arquitetura e desenvolvimento, servindo como projeto de portfólio e demonstrando competências em Python, FastAPI, PostgreSQL, Docker, autenticação, testes automatizados e documentação.