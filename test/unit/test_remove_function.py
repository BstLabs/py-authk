"""
Unit tests for remove function
"""

import os
from os import path
from unittest import TestCase, main

from authk._authorized_keys import _FILE_NAME
from authk.add import add
from authk.remove import remove

_KEY_TEXT = "".join(
    [
        "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/",
        "BWDSUGPl+nafzlHDTYW7hdI4yZ5ew18JH4JW9jbhUFrviQzM7xlELEVf4h9lFX5QVk",
        "bPppSwg0cda3Pbv7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8V6Rjs",
        "NAQwdsdMFvSlVK/7XAt3FaoJoAsncM1Q9x5+3V0Ww68/eIFmb1zuUFljQJKprrX88Xyp",
        "NDvjYNby6vw/Pb0rwert/EnmZ+AW4OZPnTPI89ZPmVMLuayrD2cE86Z/il8b+gw3r3+1",
        "nKatmIkjn2so1d01QraTlMqVSsbxNrRFi9wrf+M7Q== schacon@mylaptop.local",
    ]
)


class TestRemove(TestCase):
    """
    Unit tests for remove function
    """

    def setUp(self):
        add(_KEY_TEXT)
        self._key = _KEY_TEXT

    def tearDown(self):
        if path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

    def test_remove(self):
        remove(self._key)


if __name__ == "__main__":
    main()
