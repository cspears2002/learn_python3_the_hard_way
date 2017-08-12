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
