def solution(
    c_count: int,
    b_count: int,
    p_count: int,
    c_need_count: int,
    b_need_count: int,
    p_need_count: int,
) -> int:
    result = 0
    if c_count < c_need_count:
        result += c_need_count - c_count
    if b_count < b_need_count:
        result += b_need_count - b_count
    if p_count < p_need_count:
        result += p_need_count - p_count

    return result


if __name__ == "__main__":
    print(solution(*map(int, input().split()), *map(int, input().split())))
