import sys

count = 0

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('py'):
    sys.exit('Not a Python file')

try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.lstrip()
            if len(line) and not line.startswith('#'):
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit('File does not exist')