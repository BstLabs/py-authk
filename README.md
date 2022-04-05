# AuthK

AuthK is a lightweight Python library to handle ssh keys within authorized_keys file directly from CLI.

It's built on top of [DynaCLI](https://pypi.org/project/dynacli/) and [sshpubkeys](https://pypi.org/project/sshpubkeys/).
That makes it user friendly and secure.

AuthK was developed by [BST LABS](https://github.com/BstLabs/) as an open source generic infrastructure foundation for the cloud version of Python run-time within the scope of the [Cloud AI Operating System (CAIOS)](http://caios.io) project.

For details about the AuthK rationale and source code, refer to [AuthK](https://github.com/BstLabs/py-authk/) Github repository.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install AuthK from the PyPi site:

```bash
pip3 install authk
```

## Usage

```bash
$ authk -h
usage: authk [-h] [-v] {add, remove} ...

SSHD authorized_keys file handling utility

positional arguments:
  {add, remove}
    add        Add key to authorized_keys list
    remove     Remove key from the authorized_keys list

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

```bash
$ authk add <key_text>
<user@myhost.com> sucessfully added

$ authk remove <key_txt>
<user@myhost.com> sucessfully removed
```

## License

MIT License, Copyright (c) 2021-2022 BST LABS. See [LICENSE](LICENSE) file.
