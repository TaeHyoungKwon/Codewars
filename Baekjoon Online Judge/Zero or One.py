UPPER_ALPHABET_A = 65


def get_upper_alphabet(additional_value: int) -> str:
    return chr(UPPER_ALPHABET_A + additional_value)


def solution(targets: list[int]) -> str:

    if len(set(targets)) == 1:
        return "*"

    return (
        get_upper_alphabet(targets.index(0))
        if targets.count(1) > targets.count(0)
        else get_upper_alphabet(targets.index(1))
    )


if __name__ == "__main__":
    print(solution(list(map(int, input().split()))))
