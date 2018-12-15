# More Variables and Printig

name = 'Ádám Dénes'
age = 25 # not a lie
height = 72 # inches
weight = 163 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Dark brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's actually {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# inches to cm, pounds to kg
# pound = 0.45359237  kilograms
# inch = 2.54  centimeters

def converter (pound, inch):
    kilogram = pound * 0.45359237
    centimeter = inch * 2.54
    return kilogram, centimeter

print(converter(163, 72))
print(round(1.8333))