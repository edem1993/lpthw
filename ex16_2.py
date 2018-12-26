#!/usr/bin/env python3.4

from sys import argv

script, filename = argv

with open(filename, 'r') as f:
        print(f.read())
        f.close()