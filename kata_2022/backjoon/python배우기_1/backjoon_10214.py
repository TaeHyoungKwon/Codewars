from enum import Enum

BASE_BALL_ALL_INNING = 9


class Result(str, Enum):
    YONSEI_WIN = "Yonsei"
    KOREA_WIN = "Korea"
    DRAW = "Draw"


def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        winner = _check_winner(*_calculate_total_score())
        result.append(winner)
    return "\n".join(result)


def _check_winner(total_korea_score: int, total_yonsei_score: int) -> str:
    if total_yonsei_score > total_korea_score:
        return Result.YONSEI_WIN.value
    elif total_korea_score > total_yonsei_score:
        return Result.KOREA_WIN.value
    else:
        return Result.DRAW.value


def _calculate_total_score():
    total_yonsei_score = 0
    total_korea_score = 0
    for index in range(1, BASE_BALL_ALL_INNING + 1):
        yonsei_score, korea_score = map(int, input().split())
        total_yonsei_score += yonsei_score
        total_korea_score += korea_score
    return total_korea_score, total_yonsei_score


if __name__ == "__main__":
    print(solution())
