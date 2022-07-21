n1, n2 = map(int, input().split())
n = 1
N = n1 * n2

for i in range(int(min(n1, n2)), 1, -1):
    if (n1 % i == 0) and (n2 % i == 0):
        n = i
        N = (n1 * n2) // i
        break

print(n)
print(N)