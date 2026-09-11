from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth import router as auth_router
from app.db.database import get_db


app = FastAPI(
    title="RAGForge",
    description="Production-grade Multi-Tenant RAG Platform",
    version="0.1.0",
)


# API Routers
app.include_router(auth_router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ragforge",
    }


@app.get("/health/database")
async def database_health(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()

    return {
        "database": "connected",
        "result": value,
    }