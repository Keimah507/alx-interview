#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict

# Initialize variables to keep track of metrics
total_size = 0
status_codes = defaultdict(int)

# Read input line by line
for i, line in enumerate(sys.stdin):
    # Split line by space and extract relevant information
    line_parts = line.split()
    try:
        ip_address = line_parts[0]
        date = line_parts[3]
        request = line_parts[5]
        status_code = int(line_parts[8])
        file_size = int(line_parts[9])
    except (IndexError, ValueError):
        # Skip line if format is not as expected
        continue

    # Update metrics
    total_size += file_size
    status_codes[status_code] += 1

    # Print metrics every 10 lines or on keyboard interruption
    if i % 10 == 0 or i == KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")
