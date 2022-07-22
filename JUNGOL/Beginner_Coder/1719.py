n, m = map(int, input().split())

if n <= 100 and n % 2 == 1 and m == 1:
    for i in range(1, n // 2 + 1):
        print("*" * i)
    print("*" * (n // 2 + 1))
    for i in range(n // 2, 0, -1):
        print("*" * i)

elif n <= 100 and n % 2 == 1 and m == 2:
    for i in range(n // 2, 0, -1):
        print(" " * i, end = "")
        print("*" * (n // 2 - i + 1))
    print("*" * (n // 2 + 1))
    for i in range(1, n // 2 + 1):
        print(" " * i, end = "")
        print("*" * (n // 2 - i + 1))

elif n <= 100 and n % 2 == 1 and m == 3:
    for i in range(n, 1, -2):
        print(" " * ((n - i) // 2), end = "")
        print("*" * i)
    print(" " * (n // 2), end = "")
    print("*")
    for i in range(2, n + 1, 2):
        print(" " * ((n - i) // 2), end = "")
        print("*" * (i + 1))

elif n <= 100 and n % 2 == 1 and m == 4:
    for i in range((n // 2) + 1, 1, -1):
        print(" " * ((n // 2 + 1) - i), end = "")
        print("*" * i)
    for i in range(1, (n // 2) + 2):
        print(" " * ((n - 1) // 2), end = "")
        print("*" * i)

else:
    print("INPUT ERROR!")