import sys

from sayings import goodbye

if len(sys.argv) < 2:
    sys.exit('Enter a name: "python say.py <name>"')

# Take input provided by user and execute 'goodbye' function from saying module
elif len(sys.argv) == 2:
    goodbye(sys.argv[1])

