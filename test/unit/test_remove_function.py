"""
Unit tests for remove function
"""

import os
from os import path
from unittest import TestCase, main

from _authorized_keys import _FILE_NAME
from add import add
from remove import remove

KEY_TEXT = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/BWDSUGPl+nafzlHDTYW7hdI4yZ5ew18JH4JW9jbhUFrviQzM7xlELEVf4h9lFX5QVkbPppSwg0cda3Pbv7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8V6RjsNAQwdsdMFvSlVK/7XAt3FaoJoAsncM1Q9x5+3V0Ww68/eIFmb1zuUFljQJKprrX88XypNDvjYNby6vw/Pb0rwert/EnmZ+AW4OZPnTPI89ZPmVMLuayrD2cE86Z/il8b+gw3r3+1nKatmIkjn2so1d01QraTlMqVSsbxNrRFi9wrf+M7Q== schacon@mylaptop.local"


class TestRemove(TestCase):
    """
    Unit tests for remove function
    """

    def setUp(self):
        add(KEY_TEXT)
        self._key = KEY_TEXT

    def tearDown(self):
        if path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

    def test_remove(self):
        remove(self._key)


if __name__ == "__main__":
    main()