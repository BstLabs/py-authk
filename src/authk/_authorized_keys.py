"""
Deals with file operations. Adds functionality for context manager.
"""

import contextlib
import os
import shutil
from pathlib import Path
from typing import Final

from sshpubkeys import AuthorizedKeysFile

_FILE_NAME: Final[str] = os.path.expanduser("~/.ssh/authorized_keys")

# TODO: check for /.ssh directory existence
# TODO: check for authorized_keys permissions


class AuthorizedKeys:
    """
    Class for handling authorized_keys file.
    """

    def __init__(self):
        self._keys = {}

    def __enter__(self):
        with contextlib.suppress(FileNotFoundError):
            authk = AuthorizedKeysFile(open(_FILE_NAME, encoding="utf-8"))
            for key in authk.keys:
                self._keys[key.comment] = key
        return self._keys

    def __exit__(self, exception_type, exception_value, traceback):
        with open(_FILE_NAME, "a", encoding="utf-8") as file:
            payload = "\n".join([str(key.keydata) for key in self._keys.values()])
            file.write(payload)
        file_info = Path(_FILE_NAME)
        shutil.chown(_FILE_NAME, file_info.owner(), file_info.group())
        os.chmod(_FILE_NAME, 0o600)
        if all([exception_type, exception_value, traceback]):
            print(exception_type, exception_value, traceback, end="\n")
