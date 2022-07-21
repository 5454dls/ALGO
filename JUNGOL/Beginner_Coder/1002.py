def MIN(n1, n2):
    n = 1

    for i in range(int(min(n1, n2)), 1, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            n = i
            break
    nd.pop()
    nd.pop()
    nd.append(n)

def MAX(n1, n2):
    N = n1 * n2

    for i in range(int(min(n1, n2)), 1, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            N = (n1 * n2) // i
            break
    Nd.pop()
    Nd.pop()
    Nd.append(N)

num = int(input())
data = list(map(int, input().split()))
data.sort()

nd = data[:]
Nd = data[:]
i = num - 1
while len(nd) >= 2:
    MIN(nd[i], nd[i - 1])
    MAX(Nd[i], Nd[i - 1])
    i -= 1

print(nd[0], Nd[0])