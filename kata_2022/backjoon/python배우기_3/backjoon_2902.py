def solution():
    full_name = input()
    splited_full_name: list[str] = full_name.split("-")
    return "".join(splited_element[0] for splited_element in splited_full_name)


if __name__ == "__main__":
    print(solution())
