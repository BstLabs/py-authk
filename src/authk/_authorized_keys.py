"""
Deals with file operations. Adds functionality for context manager.
"""

import contextlib
import os
import shutil
from pathlib import Path
from typing import Final

from sshpubkeys import AuthorizedKeysFile

_SSH_DIR: Final[str] = os.path.expanduser("~/.ssh")
_FILE_NAME: Final[str] = os.path.join(_SSH_DIR, "authorized_keys")


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
        if not os.path.exists(_SSH_DIR):
            os.mkdir(_SSH_DIR)
            os.chmod(_SSH_DIR, 0o700)
            dir_info = Path(_SSH_DIR)
            shutil.chown(_SSH_DIR, dir_info.owner(), dir_info.group())
        with open(_FILE_NAME, "a", encoding="utf-8") as file:
            payload = "\n".join([str(key.keydata) for key in self._keys.values()])
            file.write(payload)
        file_info = Path(_FILE_NAME)
        shutil.chown(_FILE_NAME, file_info.owner(), file_info.group())
        os.chmod(_FILE_NAME, 0o600)
        if all([exception_type, exception_value, traceback]):
            print(exception_type, exception_value, traceback, end="\n")
