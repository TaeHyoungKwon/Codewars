from enum import Enum


class Triangle(str, Enum):
    EQUILATERAL = "Equilateral"
    ISOSCELES = "Isosceles"
    SCALENE = "Scalene"


def solution():
    angle_1 = int(input())
    angle_2 = int(input())
    angle_3 = int(input())

    if angle_1 == 60 and angle_2 == 60 and angle_3 == 60:
        return Triangle.EQUILATERAL.value

    if angle_1 + angle_2 + angle_3 == 180:
        if (angle_1 == angle_2) or (angle_2 == angle_3) or (angle_3 == angle_1):
            return Triangle.ISOSCELES.value
        else:
            return Triangle.SCALENE.value
    else:
        return "Error"


if __name__ == "__main__":
    print(solution())
