# Create a string and assign it to the formatter variable
formatter = "{} {} {} {}"

# Pass integers 1 - 4 into the format function and print the results
print(formatter.format(1, 2, 3, 4))

# Print the four strings passed to the format variable
print(formatter.format("one", "two", "three", "four"))

# Print the boolean values passed to the format variable
print(formatter.format(True, False, False, True))

# Pass the string defined in formatter to the format function four times
print(formatter.format(formatter, formatter, formatter, formatter))

# Pass these four strings to the format variable.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
