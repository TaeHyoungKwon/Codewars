from datetime import datetime


def solution(birth_day: datetime, target_day: datetime) -> str:
    age_1 = _calculator_age_1(birth_day, target_day)
    age_2 = _calculator_age_2(birth_day, target_day)
    age_3 = _calculator_age_3(birth_day, target_day)

    return "\n".join(map(str, [age_1, age_2, age_3]))


def _calculator_age_1(birth_day, target_day):
    if target_day.month > birth_day.month:
        age = target_day.year - birth_day.year
    elif target_day.month == birth_day.month:
        if target_day.day >= birth_day.day:
            age = target_day.year - birth_day.year
        else:
            age = target_day.year - birth_day.year - 1
    else:
        age = target_day.year - birth_day.year - 1

    return age


def _calculator_age_2(birth_day, target_day):
    return target_day.year - birth_day.year + 1


def _calculator_age_3(birth_day, target_day):
    return target_day.year - birth_day.year


if __name__ == "__main__":
    birth_day = datetime(*[int(ele) for ele in input().split()])
    target_day = datetime(*[int(ele) for ele in input().split()])
    print(solution(birth_day, target_day))
