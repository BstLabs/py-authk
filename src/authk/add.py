"""
Adds key to authorized_keys
"""


from _authorized_keys import AuthorizedKeys
from sshpubkeys import SSHKey


def add(key_txt: str) -> None:
    """
    Add key to authorized_keys list

    Args:
        key_txt (str): key payload in text form

    Returns:
        None

    """
    key = SSHKey(key_txt, strict=True)
    with AuthorizedKeys() as aks:
        aks[key.comment] = key
    print(f"{key.comment} succesfully added")
