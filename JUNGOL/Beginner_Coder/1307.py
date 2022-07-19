n = int(input())
arr = [[0] * n for _ in range(n)]
count= 65

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if count == 91:
            count = 65
        arr[j][i] = chr(count)
        count += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()