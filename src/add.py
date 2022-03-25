from _authorized_keys import AuthorizedKeys
from sshpubkeys import SSHKey


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
        
