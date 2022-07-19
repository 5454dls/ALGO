n = int(input())
arr = [[0] * n for _ in range(n)]
count= 65

i = 0
j = n - 1
check = 0
count = 65
while True:
    if i == n and j == n - 2:
        break
    if i == n:
        check += 1
        i = check
        j = n - 1
    if count == 91:
        count = 65
    arr[i][j] = chr(count)
    count += 1
    i += 1
    j -= 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            print(arr[i][j], end = " ")
        else:
            print(" ", end = " ")
    print()