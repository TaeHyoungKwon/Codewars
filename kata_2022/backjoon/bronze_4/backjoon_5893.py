def solution(binary_digits: str) -> str:
    return bin(int(binary_digits, 2) * 17)[2:]


if __name__ == "__main__":
    binary_digits = input()
    print(solution(binary_digits))
