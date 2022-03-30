from sshpubkeys import SSHKey

from authk._authorized_keys import AuthorizedKeys


def add(key_txt: str) -> None:
    """
    add key to authorized_keys list

    Args:
        key_txt (str): key payload in text form

    Returns:
        None

    """
    key = SSHKey(key_txt)
    with AuthorizedKeys() as aks:
        aks[key.comment] = key
    print(f"{key.comment} added")
