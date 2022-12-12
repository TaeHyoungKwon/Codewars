def solution():
    result = []
    while (encrypted_strings := input()) != "END":
        result.append(encrypted_strings[::-1])
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
