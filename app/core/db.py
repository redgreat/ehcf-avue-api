#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author by wangcw
# @generate at 2023/9/20 14:22

from app.core import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(config.DATABASE_URL_ASYNC, echo=False)

async_session = AsyncSession(
    engine, autoflush=False, autocommit=False, expire_on_commit=True
)


async def get_db():
    return async_session
