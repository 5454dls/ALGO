N = int(input())
arr = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
count = 65

def fill(n):
    global count
    i = n
    j = (2 * N - 1) // 2
    for _ in range(N - n):
        if count == 91:
            count = 65
        arr[i][j] = chr(count)
        count += 1
        i += 1
        j -= 1

    j += 2
    for _ in range(N - n - 1):
        if count == 91:
            count = 65
        arr[i][j] = chr(count)
        count += 1
        i += 1
        j += 1
    
    i -= 2
    for _ in range(N - n - 1):
        if count == 91:
            count = 65
        arr[i][j] = chr(count)
        count += 1
        i -= 1
        j += 1

    j -= 2
    for _ in range(N - n - 2):
        if count == 91:
            count = 65
        arr[i][j] = chr(count)
        count += 1
        i -= 1
        j -= 1

for i in range(N):
    fill(i)
    
for i in range(2 * N - 1):
    for j in range(2 * N - 1):
        if arr[i][j] != 0:
            print(arr[i][j], end = " ")
        else:
            print(" ", end = " ")
    print()