import argparse
from utils.file_calc import count_bytes, count_lines
from utils.reports import report

def main():
    # create parser
    parser = argparse.ArgumentParser(description="my version of wc")
    # add arguments
    parser.add_argument("filepath", type=str, help="The file to be examined.")
    parser.add_argument("-l", "--lines", action="store_true", help="count the number of lines in the file.")
    parser.add_argument("-c", "--bytes", action="store_true", help="count the number of bytes in the file.")
    # parse arguments
    args = parser.parse_args()
    #unpack filepath
    file = args.filepath
    #calculate needed details
    try:
        bytes_count = args.bytes and count_bytes(file)
        lines_count = args.lines and count_lines(file)
    except Exception:
        print(f"No such file or directory: {file}")
        return 1
    # report details
    report(file, lines_count, bytes_count)
    return 0
main()
