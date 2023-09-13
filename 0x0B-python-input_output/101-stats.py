#!/usr/bin/python3
import sys

total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

try:
    for i, line in enumerate(sys.stdin, 1):
        line = line.strip().split()
        if len(line) >= 2:
            total_file_size += int(line[-1])

            status_code = line[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        if i % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
