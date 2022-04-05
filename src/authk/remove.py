"""
Removes key from authorized_keys
"""

from sshpubkeys import SSHKey

from authk._authorized_keys import AuthorizedKeys


def remove(key_txt: str) -> None:
    """
    Remove key from the authorized_keys list

    Args:
        key_txt (str): key payload in text form

    Returns:
        None

    """
    key = SSHKey(key_txt, strict=True)
    with AuthorizedKeys() as aks:
        del aks[key.comment]
    print(f"{key.comment} sucessfully removed")
