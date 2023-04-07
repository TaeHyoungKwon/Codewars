memo = [-1] * 51


def memorize():
    memo[0] = 1
    for j in range(1, 51):
        memo[j] = memo[j - 1] * 2 + 2


def get_curve(generation: int, target_chars: str, skip: int):
    if generation == 0:
        return target_chars[skip]

    for char in target_chars:
        if char == "X" or char == "Y":
            if skip >= memo[generation]:
                skip -= memo[generation]
            elif char == "X":
                return get_curve(generation - 1, "X+YF", skip)
            else:
                return get_curve(generation - 1, "FX-Y", skip)
        elif skip > 0:
            skip -= 1
        else:
            return char


def solution(n: int, start: int, end: int) -> str:
    memorize()
    return "".join(
        get_curve(generation=n, target_chars="FX", skip=start + k - 1) for k in range(end)
    )


if __name__ == "__main__":
    #assert solution(n=0, start=1, end=2) == "FX"
    assert solution(n=1, start=1, end=5) == "FX+YF"
    #assert solution(n=2, start=6, end=5) == "+FX-Y"
    #assert solution(n=42, start=764853475, end=30) == "FX-YF-FX+YF+FX-YF-FX+YF-FX-YF-"
