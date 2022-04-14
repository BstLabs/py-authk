"""
Unit tests for _authorized_keys
"""

import os
import sys
from os import path
from unittest import TestCase, main

from authk._authorized_keys import _FILE_NAME, AuthorizedKeys


class TestAuthorizedKey(TestCase):
    """
    Class for handling unit tests
    """

    def setUp(self):
        if not os.path.isdir(_FILE_NAME.replace("authorized_keys", "")):
            os.mkdir(_FILE_NAME.replace("authorized_keys", ""))
        os.close(os.open(_FILE_NAME, os.O_RDWR | os.O_CREAT))
        if os.path.isfile(_FILE_NAME):
            with open(_FILE_NAME, "w+", encoding="utf-8"):
                print(f'{_FILE_NAME.split("/.")[-1]} created')
        else:
            print("Something wrong happened")
            sys.exit(-1)

    def tearDown(self):
        if path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

    def test_if_file_name_exists(self):
        self.assertTrue(path.isfile(_FILE_NAME), "Not file")

    def test_if_supresses_filenotfounderror(self):
        self.tearDown()
        with AuthorizedKeys() as aks:
            print(aks, type(aks))
            print("Supressed")

    def test_if_authorizedkeys_initialized_with_empty_dict(self):
        aks = AuthorizedKeys()
        self.assertEqual(type(aks._keys), dict)


if __name__ == "__main__":
    main()
