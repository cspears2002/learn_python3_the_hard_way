# Number of cars
cars = 100

# Space in a car as float.
space_in_a_car = 4.0

# Number of drivers.
drivers = 30

# Number of passengers.
passengers = 90

# The number of left over cars.
cars_not_driven = cars - drivers

# Cars with a driver.
cars_driven = drivers

# The number of passengers the cars can hold.
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers that can be in a car.
average_passengers_per_car = passengers / cars_driven

# Print the number of cars.
print("There are", cars, "cars available.")

# Print the number of drivers.
print("There are only", drivers, "drivers available.")

# Print the number of leftover cars.
print("There will be", cars_not_driven, "empty cars today.")

# Print the number of people who can be transported.
print("We can transport", carpool_capacity, "people today.")

# Print number of passengers.
print("We have", passengers, "to carpool today.")

# Print the average number of passengers that can be put in a car.
print("We need to put about", average_passengers_per_car, "in each car.")