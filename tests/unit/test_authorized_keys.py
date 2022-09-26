"""
Unit tests for _authorized_keys
"""

import os
import sys
from os import path
from pathlib import Path
from shutil import rmtree
from typing import Final
from unittest import TestCase, main

from authk._authorized_keys import AuthorizedKeys as AKS

_TEMP_DIR: Final[str] = os.path.expanduser(f"{Path.home()}/.temp_test/")
_TEMP_FILE: Final[str] = os.path.join(_TEMP_DIR, "authorized_keys")


class TestAuthorizedKey(TestCase):
    """
    Class for handling unit tests
    """

    def setUp(self):
        if not os.path.isdir(_TEMP_DIR):
            os.mkdir(_TEMP_DIR)
        os.close(os.open(_TEMP_FILE, os.O_RDWR | os.O_CREAT))
        if os.path.isfile(_TEMP_FILE):
            with open(_TEMP_FILE, "w+", encoding="utf-8"):
                print(f'{_TEMP_FILE.split("/.")[-1]} created')
        else:
            print("Something wrong happened")
            sys.exit(-1)

    def tearDown(self):
        if path.exists(_TEMP_FILE):
            os.remove(_TEMP_FILE)

    def test_if_file_name_exists(self):
        self.assertTrue(path.isfile(_TEMP_FILE), "Not file")

    def test_if_supresses_filenotfounderror(self):
        self.tearDown()
        with AKS() as aks:
            print(aks, type(aks))
            print("Supressed")

    def test_if_authorizedkeys_initialized_with_empty_dict(self):
        aks = AKS()
        self.assertEqual(type(aks._keys), dict)

    def test_creating_existing_ssh_dir(self):
        result = AKS._create_ssh_dir(_TEMP_DIR)
        assert result == "Exists"

    def test_creating_ssh_dir_success(self):
        rmtree(_TEMP_DIR)
        result = AKS._create_ssh_dir(_TEMP_DIR)
        assert result == "Success"
