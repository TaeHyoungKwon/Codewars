MESSAGE = "WelcomeToSMUPC"


def solution(n: int) -> str:
    return MESSAGE[n % len(MESSAGE) - 1]


print(solution(int(input())))
