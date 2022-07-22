N = int(input())
arr = [["0"] * N for _ in range(N)]
count = 0

def fill (i, j, check):
    global count

    di = i
    dj = j
    for _ in range(check):
        if count == 10:
            count = 0
        arr[di][dj] = count
        count += 1
        di += 1
        dj += 1

    di -= 1
    dj -= 2
    if di > i and dj >= j and check - 1 > 0:
        for _ in range(check -1):
            if count == 10:
                count = 0
            arr[di][dj] = count
            count += 1
            dj -= 1

    di -= 1
    dj += 1
    if di > i and dj >= j and check - 2 > 0:
        for _ in range(check - 2):
            if count == 10:
                count = 0
            arr[di][dj] = count
            count += 1
            di -= 1
check = N
i = 0
j = 0
while check > 0:
    fill(i, j, check)
    i += 2
    j += 1
    check -= 3

for i in range(N):
    for j in range(N):
        if arr[i][j] != "0":
            print(arr[i][j], end = " ")
    print()