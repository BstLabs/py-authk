"""
Unit tests for add function
"""


import os
from os import path
from time import sleep
from unittest import TestCase, main

from authk._authorized_keys import _FILE_NAME
from authk.add import add

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


class TestAdd(TestCase):
    """
    Unit tests for add function
    """

    def setUp(self):
        print("setting up...")
        self._key = _KEY_TEXT
        with open(_FILE_NAME, "w+", encoding="utf-8"):
            print(f'{_FILE_NAME.split("/")[-1]} created')

    def tearDown(self):
        print("tear down...")
        if path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

        print()

    def test_add(self):
        add(self._key)

    def test_doubling_key(self):
        add(self._key)
        sleep(1)
        add(self._key)


if __name__ == "__main__":
    main()
