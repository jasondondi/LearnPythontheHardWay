# the call for argv was much later in the file.
from sys import argv
script, filename = argv

# the end ' ' there prevents the print statement from adding a newline.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')

# added a prompt to save input as height
height = input()

# missing a parenthesis
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")



txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


# added math so it equals five.
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula():
    jelly_beans = start_point * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars = secret_formula()

# remember that this is another way to format a string
print("With a starting point of: {start_point}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cates = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
