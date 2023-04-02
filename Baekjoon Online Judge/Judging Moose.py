def solution(left_tine_count: int, right_tine_count: int) -> str:
    if left_tine_count == 0 and right_tine_count == 0:
        return "Not a moose"

    if left_tine_count == right_tine_count:
        return f"Even {left_tine_count + right_tine_count}"
    else:
        return f"Odd {max(left_tine_count, right_tine_count) * 2}"


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
