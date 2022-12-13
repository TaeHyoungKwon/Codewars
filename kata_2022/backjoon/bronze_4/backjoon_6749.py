def solution():
    youngest_child_age = int(input())
    middle_child_age = int(input())
    return (middle_child_age - youngest_child_age) * 2 + youngest_child_age


if __name__ == "__main__":
    print(solution())
