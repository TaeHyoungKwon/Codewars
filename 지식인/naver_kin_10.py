import random

OPERATORS = ['+', '-', '*']


def main():
    temp = []
    for _ in range(5):
        temp.append(str(random.randint(1, 10)))
        temp.append(random.sample(OPERATORS, 1)[0])
    return ' '.join(temp)


print(main())
