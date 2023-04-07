def solution(number_1: int, number_2: int) -> str:
    a = 100 - number_1
    b = 100 - number_2
    c = 100 - (a + b)
    d = a * b
    q, r = divmod(d, 100)

    result_first_line = f"{a} {b} {c} {d} {q} {r}"
    result_second_line = f"{c+q} {r}"
    return f"{result_first_line}\n{result_second_line}"


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
