# RAGForge

> Production-grade Multi-Tenant RAG Platform

RAGForge is a backend platform for building secure and scalable Retrieval-Augmented Generation (RAG) applications.

The platform is designed to support multiple tenants, document ingestion, vector search, caching, authentication, and LLM-powered question answering.

## Architecture

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
   ├── Document Ingestion
   │       ├── Parsing
   │       ├── Chunking
   │       └── Embeddings
   │
   ├── RAG Retrieval
   │       ├── Vector Search
   │       ├── Metadata Filtering
   │       └── Reranking
   │
   ├── Redis Cache
   │
   └── PostgreSQL + pgvector
           ├── Tenants
           ├── Users
           ├── Documents
           ├── Chunks
           └── Embeddings
