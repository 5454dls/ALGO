# n개 중 k개(중복순열)
def per(level):
    if level == k:
        print(p)
        return
    else:
        for i in range(n):
            p[level] = arr[i]
            per(level + 1)


n = 3
k = 2

arr = list(range(n))
p = [0] * k

per(0)