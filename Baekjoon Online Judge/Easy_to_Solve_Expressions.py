from itertools import combinations

inputs = list(map(int, input().split()))

all_case_of_input = list(combinations(inputs, 2))


all_case_of_add = list(map(lambda x: x[0] + x[1], all_case_of_input))
all_case_of_mul = list(map(lambda x: x[0] * x[1], all_case_of_input))


for input_ in inputs:
    if input_ in all_case_of_add:
        print(1)
        break
    if input_ in all_case_of_mul:
        print(2)
        break
else:
    print(3)
