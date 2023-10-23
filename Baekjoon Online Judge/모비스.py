def solution(target_string: str) -> str:
    return "NO" if any(char not in target_string for char in "MOBIS") else "YES"


if __name__ == "__main__":
    target_string = input()
    print(solution(target_string))
