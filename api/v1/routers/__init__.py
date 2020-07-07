# -*- coding: utf-8 -*-
from fastapi import APIRouter

from .common import router as common_router
from .problems import router as problems_router

router = APIRouter()

router.include_router(
    common_router,
    tags=['common'],
)

router.include_router(
    problems_router,
    prefix='/problems',
    tags=['problems'],
)
