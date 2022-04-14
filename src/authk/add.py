"""
Adds key to authorized_keys
"""

from typing import Optional

from sshpubkeys import SSHKey

from authk._authorized_keys import AuthorizedKeys


def add(key_txt: str) -> Optional[str]:
    """
    Add key to authorized_keys list

    Args:
        key_txt (str): key payload in text form

    Returns:
        None

    """
    return_value = None
    key = SSHKey(key_txt, strict=True)
    with AuthorizedKeys() as aks:
        existing_key = aks.get(key.comment)
        if existing_key:
            aks.setdefault(key.comment, key)
            print(f"{key.comment} exists")
            return_value = "exists"
        else:
            aks[key.comment] = key
            print(f"{key.comment} succesfully added")
            return_value = "sucessfully added"
    return f"{key.comment} {return_value}" if return_value else None
