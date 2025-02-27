_, x = map(int, input().split())
a = list(map(int, input().split()))
print(min(ele[0] * x + ele[1] * x for ele in list(zip(a, a[1:]))))
    