#!/usr/bin/env python3.7
# Functions and Variables

# function with 2 arguments, it will print out the arguments, when it's called
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have {} cheeses!".format(cheese_count))
	print("You have {} boxes of crackers!".format(boxes_of_crackers))
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	
	"""
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	"""

# give the function arguments directly when you call it
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# give the function variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# give it math and such...
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# combine everything
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)