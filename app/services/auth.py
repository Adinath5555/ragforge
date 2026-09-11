from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.auth import UserRegister


async def register_user(
    db: AsyncSession,
    user_data: UserRegister,
) -> User:
    existing_user = await db.execute(
        select(User).where(
            User.tenant_id == user_data.tenant_id,
            User.email == user_data.email,
        )
    )

    if existing_user.scalar_one_or_none():
        raise ValueError("User already exists")

    user = User(
        tenant_id=user_data.tenant_id,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role="member",
        is_active=True,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


async def authenticate_user(
    db: AsyncSession,
    email: str,
    password: str,
) -> User | None:
    result = await db.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        return None

    if not user.is_active:
        return None
    
    if not verify_password(password, user.password_hash):
        return None

    return user