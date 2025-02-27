import sys


for input_value in sys.stdin:
    target = int(input_value)

    if target == 0:
        break

    if target % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
