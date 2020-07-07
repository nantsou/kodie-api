# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from ..routers import router

client = TestClient(router)


def test_common_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == 'kodie-api-v1'


def test_problems_root():
    resp = client.get('/problems/')
    assert resp.status_code == 200
    assert resp.text == 'problems'
