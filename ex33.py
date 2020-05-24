i = 0
numbers = []

# while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#    print(num)

# makes a list-holder called 'numbers'
# For everything in 'numbers' that is less than 6,
# add i, and print things.
# i is a variable we set manually, starting with 0.
# every iteration, we incrememt the i variable by 1 and
# append that to the 'numbers' list.
#
# we could also do that with
#   i += i

# Convert this while-loop to a fucntion that you can call,
# and replace 6 in the test (i < 6) with a variable

# def count(upper_limit):
#    while i < upper_limit:
#        print(f"At the top i is {i}")
#        numbers.append(i)
#
#        i += i
#        print("Numbers now: ", numbers)
#        print(f"At the bottom i is {i}")

# print("Enter a number to count to:")
# upper_limit = input('> ')

# count({upper_limit})

# print("The numbers: ")

# for num in numbers:
#    print(num)

def count(arg1):
    upper_limit = int(arg1)
    i = 0

    print(f"Highest number is {upper_limit}")

    while i < upper_limit + 1:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

count(input("Enter a number to count to: "))
