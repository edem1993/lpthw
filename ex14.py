# Prompting and Passing
from sys import argv

script, user_name = argv
prompt = '-$ '

print(f"Hi {user_name}, I'm the {script} script.") 
print("I'd like to ask you a few questions.") 
print(f"Do you like me {user_name}?")
likes = input(prompt) # '> input here'

print(f"Where do you live {user_name}?")
lives = input(prompt) # '> input here'

print("What kind of computer do you have?")
computer = input(prompt) # '> input here'

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")