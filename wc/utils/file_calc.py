from os.path import getsize

def count_bytes(filepath):
    """
    counts the number of bytes in a file
    """
    return getsize(filepath)

def count_lines(filepath):
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            count += 1
    return count
