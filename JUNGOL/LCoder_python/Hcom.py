# n개 중 k개(중복조합)
def com(level, s):
    if level == k:
        print(c)
        return
    else:
        for i in range(s, n):
            c[level] = arr[i]
            com(level + 1, i)

n = 5
k = 3

arr = list(range(n))
c = [0] * k

com(0, 0)