n, m = map(int, input().split())
count = 1

for i in range(n):
    if i % 2 == 1:
        count += (m - 1)
        for j in range(m):
            print(count, end = " ")
            count -= 1
        count += (m + 1)
    else:
        for j in range(m):
            print(count, end = " ")
            count += 1
    print()