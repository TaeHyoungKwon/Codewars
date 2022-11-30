def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        first_word, second_word = input().split()
        distances = " ".join(
            str(ord(second_char) - ord(first_char))
            if second_char >= first_char
            else str((ord(second_char) + 26) - ord(first_char))
            for first_char, second_char in zip(first_word, second_word)
        )
        result.append(distances)

    return "\n".join(f"Distances: {distances}" for distances in result)


if __name__ == "__main__":
    print(solution())
