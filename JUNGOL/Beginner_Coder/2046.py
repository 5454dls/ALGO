n, m = map(int, input().split())
count = 1
if m == 1:
    for i in range(n):
        for j in range(n):
            print(count, end = " ")
        count += 1
        print()

elif m == 2:
    for i in range(n):
        if i % 2 == 1:
            count = n
            for j in range(n):
                print(count, end = " ")
                count -= 1
        else:
            count = 1
            for j in range(n):
                print(count, end = " ")
                count += 1            
        print()

else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end = " ")
        print()