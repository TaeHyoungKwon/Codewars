from enum import Enum


LIMITED_SPEED_MSG = "Congratulations, you are within the speed limit!"
NORMAL_SPEED_MSG = "You are speeding and your fine is ${fine}."


def solution(speed_limit: int, real_speed: int) -> str:
    if speed_limit >= real_speed:
        return LIMITED_SPEED_MSG

    if 1 <= real_speed - speed_limit <= 20:
        return NORMAL_SPEED_MSG.format(fine=100)
    elif 21 <= real_speed - speed_limit <= 30:
        return NORMAL_SPEED_MSG.format(fine=270)
    else:
        return NORMAL_SPEED_MSG.format(fine=500)


if __name__ == "__main__":
    print(solution(int(input()), int(input())))
