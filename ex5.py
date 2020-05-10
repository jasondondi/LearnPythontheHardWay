name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes =  'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Try to write out some variables that convert the inches and pounds
#  to centimeters and kilograms. Do not just type in the measurements
#  work out the math in Python.

metric_height = height * 2.54 # cm
# metric_height should be 187.96

metric_weight = weight * 0.45359237 # kg

print(f"Outside the USA, he is {metric_height} centimeters tall.")
print(f"Outside the USA, he is {metric_weight} kilograms heavy.")
