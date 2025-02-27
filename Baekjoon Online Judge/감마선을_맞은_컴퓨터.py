cat_picture = [input().split() for _ in range(15)]

for row in cat_picture:
    if "w" in row:
        print("chunbae")
        break
    elif "b" in row:
        print("nabi")
        break
    elif "g" in row:
        print("yeongcheol")
        break
