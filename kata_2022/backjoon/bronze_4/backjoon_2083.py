from enum import Enum


class MemberType(str, Enum):
    SENIOR = "Senior"
    JUNIOR = "Junior"

    @classmethod
    def format_junior(cls, name: str) -> str:
        return f"{name} {cls.JUNIOR.value}"

    @classmethod
    def format_senior(cls, name: str) -> str:
        return f"{name} {cls.SENIOR.value}"


def _is_senior(age: int, weight: int) -> bool:
    return age > 17 or weight >= 80


def solution(name: str, age: int, weight: int) -> str:
    return (
        MemberType.format_senior(name)
        if _is_senior(age, weight)
        else MemberType.format_junior(name)
    )


if __name__ == "__main__":
    while (input_ := input().split()) != ["#", "0", "0"]:
        name, age, weight = input_
        print(solution(name, int(age), int(weight)))
