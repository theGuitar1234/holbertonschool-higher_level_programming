#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


def print_stats(size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
