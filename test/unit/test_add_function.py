"""
Unit tests for add function
"""


import os
import sys
from os import path
from pathlib import Path
from typing import Final
from unittest import TestCase, main, mock

from authk._authorized_keys import AuthorizedKeys
from authk.add import add

_TEMP_FILE: Final[str] = os.path.expanduser(f"{Path.home()}/.temp_test/authorized_keys")

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


@mock.patch("authk._authorized_keys._FILE_NAME", _TEMP_FILE)
class TestAdd(TestCase):
    """
    Unit tests for add function
    """

    def setUp(self):
        print("setting up...")
        self._key = _KEY_TEXT
        if not os.path.isdir(_TEMP_FILE.replace("authorized_keys", "")):
            os.mkdir(_TEMP_FILE.replace("authorized_keys", ""))
        os.close(os.open(_TEMP_FILE, os.O_RDWR | os.O_CREAT))
        if os.path.isfile(_TEMP_FILE):
            with open(_TEMP_FILE, "w+", encoding="utf-8"):
                print(f'{_TEMP_FILE.split("/.")[-1]} created')
        else:
            print("Something wrong happened")
            sys.exit(-1)

    def tearDown(self):
        print("tear down...")
        if path.exists(_TEMP_FILE):
            os.remove(_TEMP_FILE)

        print()

    def test_stdout_of_add(self):
        result = add(self._key)
        assert result == "schacon@mylaptop.local sucessfully added"

    def test_result_of_double_add(self):
        add(self._key)
        result = add(self._key)
        assert result == "schacon@mylaptop.local exists"

    def test_if_aks_has_get_method(self):
        with AuthorizedKeys() as aks:
            self.assertTrue("get" in dir(aks))


if __name__ == "__main__":
    main()
