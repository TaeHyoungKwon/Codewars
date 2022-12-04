def solution():
    jaehwan = input()
    doctor = input()

    return "go" if len(jaehwan) >= len(doctor) else "no"


if __name__ == "__main__":
    print(solution())
