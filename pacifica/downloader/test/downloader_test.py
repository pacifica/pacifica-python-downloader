#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the example module."""
from shutil import rmtree
from os.path import exists, join
from tempfile import mkdtemp
from hashlib import sha1
from unittest import TestCase
from pacifica.downloader import Downloader


class TestDownloader(TestCase):
    """Test the Downloader class."""

    def test_download_cloudevent(self):
        """Test the download method in example class."""

        def sha1sum(text_data):
            """sha1sum the text_data and return string for sha1."""
            m = sha1()
            m.update(text_data)
            return m.hexdigest()
        cloud_event_stub = {
            'data': [
                {
                    'destinationTable': 'Files',
                    '_id': x,
                    'name': 'file.{}.txt'.format(x),
                    'subdir': 'subdir_{}'.format(x),
                    'hashsum': sha1sum('The data for file {}.\n'.format(x).encode('utf8')),
                    'hashtype': 'sha1'
                } for x in range(100, 110)
            ]
        }
        down_path = mkdtemp()
        down = Downloader(down_path, 'http://127.0.0.1:8081')
        down.cloudevent(cloud_event_stub)
        for x in range(100, 110):
            self.assertTrue(exists(join(down_path, 'data', 'subdir_{}'.format(x), 'file.{}.txt'.format(x))))
        rmtree(down_path)
