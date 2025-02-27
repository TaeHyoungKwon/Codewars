def solution_line_1(n: int) -> int:
    return sum(i for i in range(1, n + 1))


def solution_line_2(n: int) -> int:
    return solution_line_1(n) ** 2


def solution_line_3(n: int) -> int:
    return sum(i**3 for i in range(1, n + 1))


n = int(input())
print(solution_line_1(n))
print(solution_line_2(n))
print(solution_line_3(n))
