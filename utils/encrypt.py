from hashlib import md5, sha256
import os

def MD5(content: str) -> str:
    hash = md5()
    hash.update(content.encode())
    return hash.hexdigest()

def SHA256(content: str) -> str:
    hash = sha256()
    hash.update(content.encode()) # ignore
    return hash.hexdigest()