import math


def solution(slice_pizza: list[int], whole_pizza: list[int]) -> str:
    area, slice_pizza_price = slice_pizza
    radius, whole_pizza_price = whole_pizza

    if (area / slice_pizza_price) > (math.pi * radius**2) / whole_pizza_price:
        return "Slice of pizza"
    else:
        return "Whole pizza"


if __name__ == "__main__":

    print(
        solution(
            slice_pizza=[int(number) for number in input().split()],
            whole_pizza=[int(number) for number in input().split()],
        )
    )
