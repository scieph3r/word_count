def count_bytes(stdinbuffer):
    return len(stdinbuffer.encode())

def count_lines(stdinbuffer):
    line_count = len(stdinbuffer.split("\n"))
    return line_count - 1 if line_count > 0 else line_count

def count_characters(stdinbuffer):
    count = 0
    for line in stdinbuffer:
        count += 1
    return count

def count_words(stdinbuffer):
    return len(stdinbuffer.split())