#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Preload the archive interface for testing."""
import requests

session = requests.Session()
for i in range(100, 110):
    resp = session.put(
        'http://127.0.0.1:8080/{}'.format(i),
        data='The data for file {}.\n'.format(i)
    )
    assert resp.status_code == 201

