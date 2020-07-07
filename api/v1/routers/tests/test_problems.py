# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from ..common import router

client = TestClient(router)


def test_common_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == 'kodie-api-v1'
