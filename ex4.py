cars = 100
# space_in_a_car = 4.0
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars avaialble.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Expected output:
# There are 100 cars available.
# There are only 30 drivers available.
# There will be (100 - 30 = 70) 70 empty cars today.
# We can transport 120 people tdoay.
# We have 90 passengers to carpool today.
# We need to put about (90 / 30 = 3) in each car.
## It returns 120.0 instead of 120, and 3.0 instead of 3.
## The extra precision comes from the space_in_a_car definition.
## If I remove the .0, then I should see whole numbers in the answers.
# 4.0 is a floating point number.
