# n개 중 k개(순열)
def per(level):
    if level == k:
        print(p)
        return
    else:
        for i in range(n):
            if not visited[i]:
                p[level] = arr[i]
                visited[i] = 1
                per(level + 1)
                visited[i] = 0

n = 5
k = 3

visited = [0] * n
arr = list(range(n))
p = [0] * k

per(0)