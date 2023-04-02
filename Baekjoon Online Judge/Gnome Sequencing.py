def solution(result: list[int]) -> str:
    sorted_result = sorted(result)
    return (
        "Ordered"
        if result == sorted_result or result == sorted_result[::-1]
        else "Unordered"
    )


if __name__ == "__main__":
    case = int(input())

    print("Gnomes:")
    for _ in range(case):
        print(solution(list(map(int, input().split()))))
