a, c, e = map(int, input().split())
student_a, student_c, student_e = map(int, input().split())

if student_a == a and student_c == c and student_e == e:
    print("A")
elif student_a >= a / 2 and student_c == c and student_e == e:
    print("B")
elif student_c == c and student_e == e:
    print("C")
elif student_c >= c / 2 and student_e == e:
    print("D")
elif student_e == e:
    print("E")
else:
    raise ValueError("Invalid input")
    