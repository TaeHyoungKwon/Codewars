def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        target_strings = input()
        result.append(f"{target_strings[0]}{target_strings[-1]}")
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
