l = [[1]]
n = int(input())

for i in range(n - 1):
    tmp = [1]
    for j in range(i):
        tmp.append(l[-1][j] + l[-1][j + 1])
    tmp.append(1)
    l.append(tmp)
l.reverse()

for i in l:
    for j in i:
        print(j, end = " ")
    print()