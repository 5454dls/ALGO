n, m = map(int, input().split())
data = [[1], [1, 1]]
if 3 <= n <= 30:
    i = 3
    while i <= n:
        tmp = [1]
        for j in range(1, i - 1):
            tmp.append(data[i - 2][j - 1] + data[i - 2][j])
        i += 1
        tmp.append(1)
        data.append(tmp)

if m == 1:
    for i in data:
        for j in i:
            print(j, end = " ")
        print()    
elif m == 2:
    pro = data[::-1]
    for i in range(n):
        print(" " * i, end = "")
        for j in range(len(pro[i])):
            print(pro[i][j], end = " ")
        print()
elif m == 3:
    tmp = []
    for d1 in data[::-1]:
        for d2 in d1:
            tmp.append(d2)
    pro = [[0] * n for _ in range(n)]
    c1 = 0
    c2 = 0
    for i in range(n):
        for j in range(c1, n):
            pro[j][i] = tmp[c2]
            c2 += 1
        c1 += 1
    
    for i in range(n):
        for j in range(n):
            if pro[i][j] != 0:
                print(pro[i][j], end = " ")
        print()