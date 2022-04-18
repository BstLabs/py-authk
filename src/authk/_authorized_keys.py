"""
Deals with file operations. Adds functionality for context manager.
"""

import contextlib
import os
import shutil
from pathlib import Path
from typing import Any, Dict, Final

from sshpubkeys import AuthorizedKeysFile

_SSH_DIR: Final[str] = os.path.expanduser("~/.ssh")
_FILE_NAME: Final[str] = os.path.join(_SSH_DIR, "authorized_keys")


class AuthorizedKeys:
    """
    Class for handling authorized_keys file.
    """

    def __init__(self) -> None:
        self._keys = {}

    def __enter__(self) -> Dict[str, Any]:
        with contextlib.suppress(FileNotFoundError):
            authk = AuthorizedKeysFile(open(_FILE_NAME, encoding="utf-8"))
            for key in authk.keys:
                self._keys[key.comment] = key
        return self._keys

    def _create_ssh_dir(self, ssh_dir: str) -> str:
        if not os.path.exists(ssh_dir):
            os.mkdir(ssh_dir)
            os.chmod(ssh_dir, 0o700)
            dir_info = Path(ssh_dir)
            shutil.chown(ssh_dir, dir_info.owner(), dir_info.group())
            print(f"Missing directory created at {ssh_dir}")
        return "Success"

    def _change_file_ownership(self, file_name: str) -> None:
        file_info = Path(file_name)
        shutil.chown(file_name, file_info.owner(), file_info.group())
        os.chmod(file_name, 0o600)

    def _create_or_update_authoried_keys(self, file_name: str) -> None:
        with open(file_name, "a", encoding="utf-8") as file:
            payload = "\n".join([str(key.keydata) for key in self._keys.values()])
            file.write(payload)
        self._change_file_ownership(file_name)

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        self._create_ssh_dir(_SSH_DIR)
        self._create_or_update_authoried_keys(_FILE_NAME)
        if all([exception_type, exception_value, traceback]):
            print(exception_type, exception_value, traceback, end="\n")
