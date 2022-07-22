N = int(input())

if N <= 100 and N % 2 == 1:
    for i in range(N // 2):
        print(" " * i, end = "")
        print("*" * ((2 * i) + 1))
    print(" " * (N // 2), end = "")
    print("*" * N)
    for i in range(N // 2 - 1, -1, -1):
        print(" " * i, end = "")
        print("*" * ((2 * i) + 1)) 
else:
    print("INPUT ERROR!")