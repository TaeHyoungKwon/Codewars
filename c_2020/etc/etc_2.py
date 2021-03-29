FRUITS = {"banana", "apple"}


def get_some_fruit(fruit):
    if fruit in FRUITS:
        return fruit
    return None


if __name__ == "__main__":
    if get_some_fruit("banana") is not None:
        print("이것은 과일 입니다")
    else:
        print("이것은 과일이 아닙니다")