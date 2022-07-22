N = int(input())
arr = [[0] * N for _ in range(N)]
count = 1

def fill(n):
    global count
    i = n
    j = n
    while n <= j < N - n:
        arr[i][j] = count
        count += 1
        j += 1

    i += 1
    j = N - 1 - n
    while n <= i < N - n:
        arr[i][j] = count
        count += 1
        i += 1
    
    i = N - 1 - n
    j -= 1
    while n <= j < N - n:
        arr[i][j] = count
        count += 1
        j -= 1

    i -= 1
    j = n
    while n < i < N - n:
        arr[i][j] = count
        count += 1
        i -= 1

for i in range(N):
    fill(i)
    
for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()