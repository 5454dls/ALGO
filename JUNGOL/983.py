def func(m, n):
    if type(m) == int:
        if abs(int(m)) > abs(int(n)):
            print(m)
        else:
            print(n)
    else:
        if abs(float(m)) > abs(float(n)):
            print(n)
        else:
            print(m)

m1, n1 = map(int, input().split())
func(m1, n1)
m2, n2 = map(float, input().split())
func(m2, n2)