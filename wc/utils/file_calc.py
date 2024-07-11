from os.path import getsize

def count_bytes(filepath):
    """
    counts the number of bytes in a file
    """
    return getsize(filepath)

def count_lines(filepath):
    """
    counts the number of lines in a file
    """
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            count += 1
    return count

def count_words(filepath):
    """
    count the number of words in a file
    """
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            for wrd in line.split():
                count += 1
    return count

def count_characters(filepath):
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            count += len(line + "\n")
    return count
