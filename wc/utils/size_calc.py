from os.path import getsize

def count_bytes(filepath):
    """
    counts the number of bytes in a file
    """
    return getsize(filepath)
