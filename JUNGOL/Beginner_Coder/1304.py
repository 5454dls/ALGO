n = int(input())
count = 1

for i in range(n):
    for j in range(n):
        print(count, end = " ")
        count += n
    print()
    count -= ((n - 1) * (n + 1))