def solution(target_string: str) -> str:
    return target_string[-5:]


if __name__ == "__main__":
    _ = int(input())
    target_string = input()

    print(solution(target_string))
