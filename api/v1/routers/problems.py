# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get('/', response_class=PlainTextResponse)
async def root():
    return 'problems'
