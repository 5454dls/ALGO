N = int(input())
arr = [[0] * N for _ in range(N)]
count = 1

while count <= (N ** 2):
    if count == 1:
        nx = 0
        ny = N // 2
        arr[nx][ny] = count
    elif (count - 1) % N == 0 and nx + 1 < N:
        nx += 1
        arr[nx][ny] = count
    elif 0 <= (nx - 1) < N and 0 <= (ny - 1) < N:
        nx -= 1
        ny -= 1
        arr[nx][ny] = count
    elif (nx - 1) < 0:
        nx = N - 1
        ny -= 1
        arr[nx][ny] = count
    elif (ny - 1) < 0:
        ny = N - 1
        nx -= 1
        arr[nx][ny] = count
    count += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()