# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from ..problems import router

client = TestClient(router)


def test_problems_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == 'problems'
