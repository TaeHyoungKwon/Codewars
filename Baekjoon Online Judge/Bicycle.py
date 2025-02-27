a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t > 30:
    option1 = a + (21 * (t - 30) * x)
else:
    option1 = a

if t > 45:
    option2 = b + (21 * (t - 45) * y)
else:
    option2 = b

print(f"{option1} {option2}")
