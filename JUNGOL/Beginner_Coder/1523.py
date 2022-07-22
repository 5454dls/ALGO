n, m = map(int, input().split())

if n <= 100 and m == 1:
    for i in range(1, n + 1):
        print("*" * i)
elif n <= 100 and m == 2:
    for i in range(n, 0, -1):
        print("*" * i)
elif n <= 100 and m == 3:
    for i in range(n):
        print(" " * (n - i - 1), end = "")
        print("*" * (2 * i + 1))
else:
    print("INPUT ERROR!")