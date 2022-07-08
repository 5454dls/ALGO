N, M = map(int, input().split())
l = [0] * N
arr = list(range(1, 7))

def func(level):
    if level == N:
        if sum(l) == M:
            for n in l:
                print(n, end = " ")
            print()
        return
    else:
        for i in range(6):
            l[level] = arr[i]
            func(level + 1)

func(0)