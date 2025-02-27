input_value = input().split()
lv, panjung = int(input_value[0]), input_value[1]

if panjung == "miss":
    print(0)
elif panjung == "bad":
    print(lv * 200)
elif panjung == "cool":
    print(lv * 400)
elif panjung == "great":
    print(lv * 600)
else:
    print(1000 * int(lv))
    