#!/usr/bin/env python3.4
# Names, Variables, Code, Function

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
#	print(f"arg1: {arg1}, arg2: {arg2}")
	print("arg1: {}, arg2: {}".format(arg1, arg2))
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
#	print(f"arg1: {arg1}, arg2: {arg2}")
	print("arg1: {}, arg2: {}".format(arg1, arg2))
	
# this just takes one argument
def print_one(arg1):
#	print(f"arg1: {arg1}")
	print("arg1: {}".format(arg1))
	
# this one takes no arguments
def print_none():
	print("I got nothin'.")
	
print_two("Jon", "Doe")
print_two_again("Jon", "Doe")
print_one("First!")
print_none()