def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        sentence = input()
        result.append(f"{sentence[0].upper()}{sentence[1:]}")

    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
