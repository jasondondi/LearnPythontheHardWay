# Write a line that tells us what you're about to do:
# print "I will now count my chickens:"

# Do math - I don't know why you add hens and divide by 6, but there you go.
# print "Hens", 25.0 + 30.0 / 6.0
# print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

# print "Now I will count the eggs:"

# print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

# print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"

# print 3.0 + 2.0 < 5.0 - 7.0

# print "What is 3.0 + 2.0?", 3.0 + 2.0
# print "What is 5.0 - 7.0?", 5.0 - 7.0

# print "Oh, that's why it's False."

# print "How about some more."

# print "Is it greater?", 5.0 > -2.0
# print "Is it greater or equal?", 5.0 >= -2.0
# print "Is it less or equal?", 5.0 <= -2.0

# Now for python3:

# This will print the text
print("I will now count my chickens:")

# This will print the word "Hens" and then do math
# It will divide 30 / 6 = 5 then add 25, = 30.
print("Hens", 25 + 30 / 6)

# This one will multiply 25 * 3 = 75. 75 % 4 = 3
# and 100 - 3 = 97
# -- but what -is- percent?
# Percent is the Modulus: returns the remainder when first operand
#      is divided by the second.
print("Roosters", 100 - 25 * 3 % 4)

# This prints the text.
print("Now I will count the eggs:")

# This does math.
# 3 + 2 + 1 - 5 + (4 % 2 = 0) - (1 / 4 = 0.25) + 6
# 1 + 0 - 0.25 + 6
# 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# just prints text.
print("Is it true that 3 + 2 < 5 - 7?")

# 5 < -2 ... see the next
print(3 + 2 < 5 - 7)

# Prints some text and does some math; prints math after text.
# Automatically adds a space between the text string and the math print.
# These print numbers because they do math
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

# print text
print("Oh, that's why it's False.")

# print text
print("How about some more.")

#  These print "True" or "False" because they do evaluations, not math.
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
