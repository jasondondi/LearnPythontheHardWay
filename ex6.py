# Set a variable 'x' to be the statement
# There are 10 types of people. Where most of it is in the quoted literal,
# and %d takes the information provided at the end, which is 10. 

x = "There are %d types of people." % 10


#fill a variable named binary with the word 'binary'
binary = "binary"
do_not = "don't" 
# %d pulls digit, %s pulls string. What was %r called?
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This shows how I can store a string into a variable, 
# store a... whatever %r is, and call them like this 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#jams the two variables together with no extra spacing added.
print w + e

#The difference between %r (raw) and %s (string): 
# We use %r for debugging because it displas the 'raw' data of the variable. 
# but we use %s and others for displaying to users. 

