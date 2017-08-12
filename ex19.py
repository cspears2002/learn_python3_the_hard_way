# Define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print the number of cheeses
    print(f"You have {cheese_count} cheeses!")

    # Print the number of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")

    # Print a statement
    print("Man that's enough for a party!")

    # Print a statement
    print("Get a blanket.\n")

# Print a statement
print("We can just give the function numbers directly:")
# Pass 20 and 30 to cheese_and_crackers
cheese_and_crackers(20, 30)

# Print a statement
print("OR, we can use variables from our script:")
# Define a variable
amount_of_cheese = 10
# Define a variable
amount_of_crackers = 50

# Pass those variables to cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a statement
print("We can even do math inside too:")

# Pass the results of addition into cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# Print a statement
print("And we can combine the two, variables and math:")

# Pass the results of addition into cheese_and_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def area_of_rectangle(length, width):
    return float(length) * float(width)

# 1
print(area_of_rectangle(1, 2))

# 2
print(area_of_rectangle(2.5, 2))

# 3
print(area_of_rectangle(3.0, 1.0))

# 4
print(area_of_rectangle(2+3, 1+3))

# 5
print(area_of_rectangle(3-2, 4-3))

# 6
length = 1
width = 2
print(area_of_rectangle(length, width))

# 7
print(area_of_rectangle(length+1, width+2))

# 8
print(area_of_rectangle(width, length))

# 9
some_number = 3
another_number = 4
print(area_of_rectangle(some_number, another_number))

# 10
print(area_of_rectangle(another_number * 100, some_number * 50))
