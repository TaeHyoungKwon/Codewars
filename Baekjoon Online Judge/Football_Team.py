import sys

translation = str.maketrans({"i": "e", "e": "i", "I": "E", "E": "I"})

for line in sys.stdin:
    print(line.rstrip("\n").translate(translation))
