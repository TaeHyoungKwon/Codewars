input_ = input()

result = [''.join(x) for x in zip(input_[::2], input_[1::2])]

a = 0
b = 0

for ele in result:
    if ele[0] == "A":
        a += int(ele[1])
    else:
        b += int(ele[1])
        
    if a >= 10 and b >= 10 and abs(a-b) >= 2:
        break

if a > b:
    print("A")
else:
    print("B")
