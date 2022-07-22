N = int(input())
arr = [[0] * N for _ in range(N)]
count = 1

for i in range(N):
    if i % 2 == 1:
        j = i
        k = 0
        while j >= 0:
            arr[j][k] = count
            count += 1
            j -= 1
            k += 1
    else:
        j = 0
        k = i
        while k >= 0:
            arr[j][k] = count
            count += 1
            j += 1
            k -= 1

if N % 2 == 1:
    check = 0
else:
    check = 1

for i in range(N - 1):
    if i % 2 == check:
        j = N - 1
        k = i + 1
        while k < N:
            arr[j][k] = count
            count += 1
            j -= 1
            k += 1
    else:
        j = i + 1
        k = N - 1
        while j < N:
            arr[j][k] = count
            count += 1
            j += 1
            k -= 1

for d1 in arr:
    for d2 in d1:
        print(d2, end = " ")
    print()