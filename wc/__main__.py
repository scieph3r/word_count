import argparse
from utils.file_calc import count_bytes, count_lines, count_words
from utils.reports import report
from sys import argv

def main():
    # create parser
    parser = argparse.ArgumentParser(description="my version of wc")
    # add arguments
    parser.add_argument("filepath", type=str, help="The file to be examined.")
    parser.add_argument("-w", "--words", action="store_true", help="count the number of words in the file.")
    parser.add_argument("-l", "--lines", action="store_true", help="count the number of lines in the file.")
    parser.add_argument("-c", "--bytes", action="store_true", help="count the number of bytes in the file.")
    # parse arguments
    args = parser.parse_args()
    #unpack filepath
    file = args.filepath
    # default state
    if len(argv) == 2:
        args.words = True
        args.bytes = True
        args.lines = True
    # calculate needed details
    try:
        word_count = args.words and count_words(file)
        bytes_count = args.bytes and count_bytes(file)
        lines_count = args.lines and count_lines(file)
    except Exception:
        print(f"No such file or directory: {file}")
        return 1
    # report details
    report(file, word_count, lines_count, bytes_count)
    return 0
main()
