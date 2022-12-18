def solution(sum_of_result: int, sub_of_result: int) -> str:
    a = (sum_of_result + sub_of_result) // 2
    b = sum_of_result - a
    return " ".join(map(str, sorted([a, b], reverse=True)))


def is_valid(sum_of_result: int, sub_of_result: int) -> bool:
    return (
        sum_of_result + sub_of_result >= 0
        and sum_of_result - sub_of_result >= 0
        and (sum_of_result + sub_of_result) % 2 == 0
    )


if __name__ == "__main__":
    input_ = [int(number) for number in input().split()]
    if not is_valid(*input_):
        print(f"-1")
    else:
        print(solution(*input_))
