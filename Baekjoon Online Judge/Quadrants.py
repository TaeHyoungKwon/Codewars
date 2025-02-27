import sys

for input_values in sys.stdin:
    x, y = [float(ele) for ele in input_values.split()]
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")
    else:
        print("AXIS")
