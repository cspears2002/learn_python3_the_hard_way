# Set the number of people
people = 30
# Set the number of cars
cars = 40
# Set the number of trucks
trucks = 15

# If we have more cars than people
if cars > people:
# then print this message
    print("We should take the cars.")
# If we have more people than cars
elif cars < people:
# then print this message
    print("We should not take the cars.")
# Otherwise print the message below.
# This would probably only happen if the number
# of cars is equal to the number of people
else:
    print("We can't decide.")

# If we have more trucks than cars
if trucks > cars:
# print this message
    print("That's too many trucks.")
# If we more cars than trucks
elif trucks < cars:
# print this message
    print("Maybe we could take the trucks.")
# Otherwise print the message below.
# This would probably only happen if the number
# of trucks is equal to the number of cars
else:
    print("We still can't decide.")

# If we have more people than trucks
if people > trucks:
# then print this message
    print("Alright, let's just take the trucks.")
# Otherwise print this message
else:
    print("Fine, let's stay home then.")
