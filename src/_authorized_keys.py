import os
import shutil
from typing import Final
from sshpubkeys import AuthorizedKeysFile


_FILE_NAME: Final[str] = '/home/ssm-user/.ssh/authorized_keys' 


class AuthorizedKeys:
    def __enter__(self):
        self._keys = dict()
        try:
            authk = AuthorizedKeysFile(open(_FILE_NAME))
            for key in authk.keys:
                self._keys[key.comment] = key
        except FileNotFoundError:
            pass
        return self._keys

    def __exit__(self, exception_type, exception_value, traceback):
        with open(_FILE_NAME, 'w') as f:
            payload = '\n'.join((f"{key.keydata}" for key in self._keys.values()))
            f.write(payload)
        shutil.chown(_FILE_NAME, 'ssm-user', 'ssm-user')
        os.chmod(_FILE_NAME, 0644)

