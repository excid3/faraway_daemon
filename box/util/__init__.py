import hashlib
from memoize import memoize

def digest(content):
    return hashlib.md5(content).hexdigest()
