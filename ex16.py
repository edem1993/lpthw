#!/usr/bin/env python3.4
# Reading and Writing Files

from sys import argv

script, filename = argv

# print(f"We're going to erase {filename}.")
print("We're going to erase {}.".format(filename))      # Format string
print("If you don't want that, hit CTRL-C (^C).")       # Stop or Start
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')    # assign the opened file to a new variable

print("Truncating the file. Goodbye!")
target.truncate()               # truncate the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")       # ask for input
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("{}\n{}\n{}".format(line1, line2, line3))
"""
target.write(line1)             # write the input in the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
print("And finally, we close it.")
target.close()                  # close the file
