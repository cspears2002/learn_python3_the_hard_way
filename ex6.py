# Set this variable to 10.
types_of_people = 10

# Create a f string.
# String in a string.
x = f"There are {types_of_people} types of people."

# Set binary to a string.
binary = "binary"

# Set do_not to a string.
do_not = "don't"

# Create a f string.
# String in a string.
y = f"Those who know {binary} and those who {do_not}."

# Print variable x.
print(x)

# Print variable y.
print(y)

# Print a string.
# String in a string.
print(f"I said: {x}")

# Print a string.
# String in a string.
print(f"I also said: '{y}'")

# Set a variable to a boolean. 
hilarious = False

# Set joke_evaluation to a string.
# This will be evaluated later.  String in a string.
joke_evaluation = "Isn't that joke so funny?! {}"

# Add the hilarious variable to joke_evaluation.
print(joke_evaluation.format(hilarious))

# Set w to a string.
w = "This is the left side of..."

# Set e to a string.
e = "a string with a right side."

# Print w and e.
print(w + e)
