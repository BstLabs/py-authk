#!/usr/bin/env python3

"""
SSHD authorized_keys file handling utility
"""


import os
import sys

from dynacli import main as dynamain

cwd = os.path.dirname(os.path.realpath(__file__))


search_path = [cwd]
sys.path.extend(search_path)

_map = {
    "__version__": "1.0.3",
    "__doc__": """
SSHD authorized_keys file handling utility""",
}


def _set_main_attrs(**kwargs):
    _main = sys.modules["__main__"]
    for key, val in kwargs.items():
        setattr(_main, key, val)


# For package distro purposes
def main():
    _set_main_attrs(**_map)
    dynamain(search_path)


if __name__ == "__main__":
    main()
