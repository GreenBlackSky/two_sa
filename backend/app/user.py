"""
User logic stuff.

This module contains methods to create new user or
to get access to existing one.
"""

from hashlib import md5

from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from .utils.exceptions import LogicException
from .utils.models import UserModel

from .utils.database import get_session


router = APIRouter()


async def authorized_user(
    authorize: AuthJWT = Depends(),
    async_session: sessionmaker = Depends(get_session),
) -> UserModel:
    authorize.jwt_required()
    user_id = authorize.get_jwt_subject()
    async with async_session() as session:
        return await session.get(UserModel, user_id)


class UserRequest(BaseModel):
    name: str
    password: str


@router.post("/register")
async def register(
    user_data: UserRequest,
    authorize: AuthJWT = Depends(),
    async_session: sessionmaker = Depends(get_session),
):
    """Register new user."""
    pass


@router.post("/login")
async def login(
    user_data: UserRequest,
    authorize: AuthJWT = Depends(),
    async_session: sessionmaker = Depends(get_session),
):
    """Log in user."""
    pass


class EditUserRequest(BaseModel):
    name: str
    old_pass: str
    new_pass: str


@router.post("/edit_user")
async def edit_user(
    user_data: EditUserRequest,
    current_user: UserModel = Depends(authorized_user),
    async_session: sessionmaker = Depends(get_session),
):
    """Edit user."""
    pass


@router.post("/logout")
async def logout(Authorize: AuthJWT = Depends()):
    """Log out user."""
    pass
