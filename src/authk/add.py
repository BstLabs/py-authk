"""
Adds key to authorized_keys
"""


from sshpubkeys import SSHKey

from authk._authorized_keys import AuthorizedKeys


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
        existing_key = aks.get(key.comment)
        if not existing_key:
            aks[key.comment] = key
            print(f"{key.comment} succesfully added")
        elif existing_key & existing_key != key:
            aks[key.comment] = key
            print(f"{key.comment} succesfully updated")
