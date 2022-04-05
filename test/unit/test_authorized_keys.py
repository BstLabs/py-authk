"""
Unit tests for _authorized_keys
"""

import os
from os import path
from unittest import TestCase, main

from authk._authorized_keys import _FILE_NAME, AuthorizedKeys


class TestAuthorizedKey(TestCase):
    """
    Class for handling unit tests
    """

    def setUp(self):
        with open(_FILE_NAME, "w+", encoding="utf-8"):
            print(_FILE_NAME.split("/")[-1])

    def tearDown(self):
        if path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

    def test_if__FILE_NAME_exists(self):
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
