# RAGForge

> Production-grade Multi-Tenant RAG Platform

RAGForge is a backend platform for building secure and scalable **Retrieval-Augmented Generation (RAG)** applications.

The platform is designed to support multiple tenants, document ingestion, vector search, caching, authentication, and LLM-powered question answering.

## Target Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Authentication & Authorization
   │
   ├── Multi-Tenant Isolation
   │
   ├── Document API
   │      │
   │      └── Object Storage
   │
   ├── RAG Query API
   │
   └── Rate Limiting
          │
          ▼
       Redis
          │
          ├── Cache
          └── Job Queue
                  │
                  ▼
            Background Workers
                  │
                  ├── Document Parsing
                  ├── Text Chunking
                  ├── Embedding Generation
                  └── Document Indexing
                          │
                          ▼
                 PostgreSQL + pgvector
                          │
                          ├── Tenants
                          ├── Users
                          ├── Documents
                          ├── Chunks
                          └── Embeddings

RAG Query
   │
   ▼
Retrieval Pipeline
   │
   ├── Vector Search
   ├── Metadata Filtering
   ├── Reranking
   └── Context Construction
          │
          ▼
     LLM Provider
          │
          ▼
     Grounded Answer
          │
          └── Source Citations
```

## Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy 2.0**
- **PostgreSQL**
- **pgvector**
- **Redis**
- **Alembic**
- **Docker**
- **Pytest**
- **JWT Authentication**

## Current Features

- FastAPI backend
- Async SQLAlchemy database layer
- PostgreSQL with pgvector
- Redis infrastructure
- Environment-based configuration
- Alembic database migrations
- Multi-tenant database architecture
- Tenant model
- User model
- Tenant-scoped user uniqueness
- Database health checks
- Docker Compose development environment
- Secure password hashing with Argon2
- User registration API foundation

## Planned Features

### Authentication

- User registration
- User login
- JWT access tokens
- Secure password hashing
- Role-based access control
- Tenant isolation
- Protected API endpoints

### Document Processing

- PDF ingestion
- DOCX ingestion
- TXT ingestion
- Text extraction
- Document chunking
- Background processing
- Embedding generation
- Document indexing

### RAG Pipeline

- Vector similarity search
- Metadata filtering
- Hybrid retrieval
- Reranking
- Context construction
- LLM provider abstraction
- Source citations
- Grounded responses

### Production Engineering

- Redis caching
- Rate limiting
- Request validation
- Pagination
- Idempotency
- Structured logging
- Centralized exception handling
- Automated testing
- Integration testing
- CI/CD
- Observability
- Performance testing

## Project Structure

```text
ragforge/
│
├── app/
│   ├── api/
│   │   └── auth.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── tenant.py
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── auth.py
│   │   └── __init__.py
│   │
│   └── main.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/
│
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
└── README.md
```

## Local Development

### Prerequisites

- Python 3.12+
- Docker Desktop
- Git

### Clone the Repository

```bash
git clone https://github.com/Adinath5555/ragforge.git
cd ragforge
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file using `.env.example` as a reference.

Never commit `.env` or production secrets to Git.

### Start Infrastructure

```bash
docker compose up -d
```

This starts:

- PostgreSQL + pgvector
- Redis

### Run Database Migrations

```bash
alembic upgrade head
```

### Start the API

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Database Migrations

Create a migration:

```bash
alembic revision --autogenerate -m "migration description"
```

Apply migrations:

```bash
alembic upgrade head
```

Check migration status:

```bash
alembic current
```

## API Endpoints

### Health Check

```http
GET /health
```

### Database Health Check

```http
GET /health/database
```

### User Registration

```http
POST /auth/register
```

## Security

RAGForge follows security-oriented backend practices including:

- Password hashing using **Argon2**
- Environment-based secrets
- Tenant-aware data isolation
- Database-level constraints
- JWT-based authentication architecture
- No plaintext password storage
- Secrets excluded from Git

## Engineering Goals

RAGForge is being developed around production backend engineering principles:

- **Async I/O**
- **Database connection pooling**
- **Multi-tenant data isolation**
- **Version-controlled database migrations**
- **Secure authentication**
- **Horizontal scalability**
- **Caching**
- **Background processing**
- **Observability**
- **Automated testing**
- **Containerized infrastructure**
- **Clean service-layer architecture**

## Development Roadmap

```text
[x] FastAPI foundation
[x] Docker infrastructure
[x] PostgreSQL + pgvector
[x] Redis
[x] Async SQLAlchemy
[x] Environment configuration
[x] Alembic migrations
[x] Tenant model
[x] User model
[x] Password hashing
[x] Registration API foundation

[ ] JWT authentication
[ ] RBAC
[ ] Tenant API
[ ] Document management
[ ] Document ingestion
[ ] Background workers
[ ] Embedding pipeline
[ ] Vector retrieval
[ ] RAG query pipeline
[ ] LLM integration
[ ] Redis caching
[ ] Rate limiting
[ ] Automated tests
[ ] CI/CD
[ ] Observability
[ ] Production deployment
```

## License

This project is currently a personal engineering project and portfolio demonstration.
