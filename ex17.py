from sys import argv

# we could do these two on one line, how?
open(argv[2], 'w').write(open(argv[1]).read())
