l = list(map(int, input().split()))
n = l[0] * l[1] * l[2]
l = list(str(n))

def func(s, result):
    if s == len(l):
        print(result)
    else:
        if int(l[s]) != 0:
            result *= int(l[s])
        func(s + 1, result)

func(0, 1)