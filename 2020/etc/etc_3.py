FRUITS = {"banana", "apple"}


def set_some_fruit(fruit):
    fruits = []
    if is_fruit(fruit):
        fruits.append(fruit)


if __name__ == "__main__":
    if get_some_fruit("banana") is not None:
        print("이것은 과일 입니다")
    else:
        print("이것은 과일이 아닙니다")