import argparse
from utils.size_calc import count_bytes
from utils.reports import report

def main():
    # create parser
    parser = argparse.ArgumentParser(description="my version of wc")
    # add arguments
    parser.add_argument("filepath", type=str, help="The file to be examined.")
    parser.add_argument("-c", "--bytes", action="store_true", help="count the number of bytes in the file.")
    # parse arguments
    args = parser.parse_args()
    #unpack filepath
    file = args.filepath
    #calculate needed details
    try:
        bytes_count = args.bytes and count_bytes(file)
    except Exception:
        print(f"No such file or directory: {file}")
        return 1
    # report details
    report(file, bytes_count)
    return 0
main()
