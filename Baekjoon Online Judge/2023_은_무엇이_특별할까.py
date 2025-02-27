count = int(input())

for _ in range(count):
    number = int(input())
    target = number + 1
    if target % int(str(number)[-2:]) == 0:
        print("Good")
    else:
        print("Bye")
