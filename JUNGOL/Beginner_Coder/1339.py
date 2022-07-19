n = int(input())
arr = [[0] * n for _ in range(n)]
count= 65

i = (n // 2)
j = (n // 2)
check = 0
count = 65
while True:
    if n < 1 or n > 100 or n % 2 == 1:
        print("INPUT ERROR")
        break
    if i == (n // 2) - check and j == -1:
        break
    if count == 91:
        count = 65
    arr[i][j] = chr(count)
    count += 1
    if i == (n // 2) + check:
        check += 1
        i = (n // 2) - check
        j -= 1
    else:
        i += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            print(arr[i][j], end = " ")
        else:
            print(" ", end = " ")
    print()