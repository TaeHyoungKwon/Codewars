def solution(inputs: list[int]) -> str:
    return "\n".join(count * "=" for count in inputs)


if __name__ == "__main__":
    case_count = int(input())
    print(solution([int(input()) for _ in range(case_count)]))
