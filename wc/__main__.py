import argparse
from utils.file_calc import count_bytes, count_lines, count_words, count_characters
import utils.stdin_calc as stdin_calc
from utils.reports import report
from sys import argv, stdin

def main():
    # create parser
    parser = argparse.ArgumentParser(description="my version of wc")
    # add arguments
    parser.add_argument("filepath", type=str, nargs="?", help="The file to be examined.")
    parser.add_argument("-v", "--version", action="store_true", help="display program version.")
    parser.add_argument("-m", "--chars", action="store_true", help="count the number of characters in the file.")
    parser.add_argument("-w", "--words", action="store_true", help="count the number of words in the file.")
    parser.add_argument("-l", "--lines", action="store_true", help="count the number of lines in the file.")
    parser.add_argument("-c", "--bytes", action="store_true", help="count the number of bytes in the file.")
    # parse arguments
    args = parser.parse_args()
    # unpack filepath
    file = args.filepath
    # creation details
    if args.version:
        print("""
word_count v1.0.0
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

written by: Scieph3r
              """)
        return 0
    # default state
    if args.filepath != None and len(argv) == 2:
        args.words = True
        args.bytes = True
        args.lines = True
    # calculate needed details
    word_count = False
    byte_count = False
    line_count = False
    char_count = False
    # filepath provided
    if file:
        try:
            word_count = args.words and count_words(file)
            byte_count = args.bytes and count_bytes(file)
            line_count = args.lines and count_lines(file)
            char_count = args.chars and count_characters(file)
        except Exception:
            print(f"No such file or directory: {file}")
            return 1
    # stdin provided
    else:
        stdinput = stdin.read()
        try:
            word_count = args.words and stdin_calc.count_words(stdinput)
            byte_count = args.bytes and stdin_calc.count_bytes(stdinput)
            line_count = args.lines and stdin_calc.count_lines(stdinput)
            char_count = args.chars and stdin_calc.count_characters(stdinput)
        except Exception:
            print("Something went wrong:(")
            return 1

    # report details
    print("  ", end="")
    report(file, line_count, word_count, char_count, byte_count)
    return 0
main()
