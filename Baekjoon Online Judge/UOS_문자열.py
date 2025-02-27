TARGET_STRING = "UOS"

x = int(input())

if x % 3 == 1:
    print(TARGET_STRING[0])
elif x % 3 == 2:
    print(TARGET_STRING[1])
else:
    print(TARGET_STRING[2])
