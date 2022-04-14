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

    def _set_up_file(self, ssh_dir, file_name):
        if not os.path.exists(ssh_dir):
            os.mkdir(ssh_dir)
            os.chmod(ssh_dir, 0o700)
            dir_info = Path(ssh_dir)
            shutil.chown(ssh_dir, dir_info.owner(), dir_info.group())
        with open(file_name, "a", encoding="utf-8") as file:
            payload = "\n".join([str(key.keydata) for key in self._keys.values()])
            file.write(payload)
        file_info = Path(file_name)
        shutil.chown(file_name, file_info.owner(), file_info.group())
        os.chmod(file_name, 0o600)

    def __exit__(self, exception_type, exception_value, traceback):
        self._set_up_file(_SSH_DIR, _FILE_NAME)
        if all([exception_type, exception_value, traceback]):
            print(exception_type, exception_value, traceback, end="\n")
