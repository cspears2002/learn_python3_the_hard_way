from sys import argv

script, filename = argv

my_file = open(filename)
print(my_file.read())

my_file.close()
