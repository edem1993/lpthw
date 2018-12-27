#!/usr/bin/env python3.4
# More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")
print("Copying from {} to {}".format(from_file, to_file))

indata = open(from_file).read()

# print(f"The input file is {len(indata)} bytes long.")
print("The input file is {} bytes long.".format(len(indata)))

# print(f"Does the output file exist? {exists(to_file)}")
print("Does the output file exist? {}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()