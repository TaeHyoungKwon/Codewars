def solution(target_string: str, index_: int) -> str:
    return target_string[index_ - 1]


if __name__ == "__main__":
    target_string = input()
    index_ = int(input())
    print(solution(target_string, index_))
