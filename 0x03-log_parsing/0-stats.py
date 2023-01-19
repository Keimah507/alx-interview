#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys

if __name__ == "__main__":
    file_size = [0]
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 1


    def print_stats():
        """prints the stats to output"""
        print("File size: {}".format(file_size[0]))

        for code in sorted((status_code_count.keys())):
            if status_code_count[code] != 0:
                print("{}: {}".format(code, status_code_count[code]))


    def parse_stdin(line):
        """parses the input from stdin"""
        try:
            line = line[:-1]
            word = line.split(' ')
            file_size[0] += int(word[-1])
            status_code = int(word[-2])
            if status_code in status_code_count:
                status_code_count[status_code] += 1
        except BaseException:
            pass

    try:
        for line in sys.stdin:
            parse_stdin(line)
        if line_count % 10 == 0:
            print_stats()
        line_count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
