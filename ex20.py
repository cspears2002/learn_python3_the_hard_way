# Import argv from sys
from sys import argv

# argv holds the name of the script and the first argument
script, input_file = argv

# Define a function
def print_all(f):
    # Print everything in a file
    print(f.read())

# Define a function
def rewind(f):
    # "Rewind" the file so it starts at the beginning
    f.seek(0)

# Define a function
def print_a_line(line_count, f):
    # Print line_count and a line from the file
    print(line_count, f.readline())

# Open the file
current_file = open(input_file)

# Print statement
print("First let's print the whole file:\n")

# Print out everything in the newly opened file
print_all(current_file)

# Print statement
print("Now let's rewind, kind of like a tape.")

# Rewind the file
rewind(current_file)

# Print statement
print("Let's print three lines:")

# Set the current_line variable to 1
current_line = 1
# Print the first line from the file
print_a_line(current_line, current_file)

# Current line is 2
current_line += 1
# Print the second line from the file
print_a_line(current_line, current_file)

# Current line is 3
current_line += 1
# Print the third line from the file
print_a_line(current_line, current_file)
