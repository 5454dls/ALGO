n, m = map(int, input().split())

if n <= 100 and n % 2 == 1 and m == 1:
    arr = [[0] * n for _ in range(n)]
    count = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(i + 1):
                arr[i][j] = count
                count += 1
        else:
            for j in range(i, -1, -1):
                arr[i][j] = count
                count += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                print(arr[i][j], end = " ")
        print()

elif n <= 100 and n % 2 == 1 and m == 2:
    for i in range(n):
        print("  " * i, end = "")
        print((str(i) + " ") * (((n - i) * 2) - 1) , end = " ")
        print()

elif n <= 100 and n % 2 == 1 and m == 3:
    for i in range(n // 2):
        for j in range(1, i + 2):
            print(j, end = " ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(1, i + 2):
            print(j, end = " ")
        print()

else:
    print("INPUT ERROR!")