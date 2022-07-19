a, b = map(int, input().split())

for i in range(1, 10):
    if a > b:
        for j in range(a, b - 1, -1):
            result = f"{i * j}".rjust(2)
            print(f"{j} * {i} ={result}", end = "   ")
    else:
        for j in range(a, b + 1):
            result = f"{i * j}".rjust(2)
            print(f"{j} * {i} ={result}", end = "   ")
    print()