# -*- coding: utf-8 -*-
from fastapi import FastAPI

from api import v1

app = FastAPI()

app.include_router(
    v1.router,
    prefix='/v1',
    tags=['v1'],
)
