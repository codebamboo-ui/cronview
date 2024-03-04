#!/usr/bin/env python3
import random
from datetime import datetime, timedelta
import sys

# Utility to print a plausible next commit time based on a previous one.

def main():
    if len(sys.argv) != 2:
        print("usage: next-commit-time.py <prev-iso>", file=sys.stderr)
        sys.exit(1)
    prev = datetime.fromisoformat(sys.argv[1])
    # Between 4h and 5 days, with random seconds
    delta = timedelta(seconds=random.randint(4*3600, 5*24*3600))
    print((prev + delta).strftime('%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    main()

