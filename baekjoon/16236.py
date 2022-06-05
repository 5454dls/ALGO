import collections

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
fish = []

for i in range(N):
    for j in range(N):
        if 0 < arr[i][j] <= 6:
            fish.append((i, j))
        elif arr[i][j] == 9:
            sx, sy = i, j

size = 2
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
arr[sx][sy] = 0

def bfs(sx, sy):
    stack = collections.deque([(sx, sy, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1

    dist_list = []
    min_dist = N * N * N
    while stack:
        x, y, dist = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] <= size:
                visited[nx][ny] = 1
                if 0 < arr[nx][ny] < size:
                    min_dist = dist
                    dist_list.append((nx, ny, dist + 1))
                if dist + 1 <= min_dist:
                    stack.append((nx, ny, dist + 1))
    if dist_list:
        dist_list.sort(key = lambda x: x[1])
        dist_list.sort(key = lambda x: x[0])
        dist_list.sort(key = lambda x: x[2])
        return dist_list[0]
    else:
        return False

eat = 0
time = 0
num_fish = len(fish)

while num_fish:
    eating = bfs(sx, sy)
    if not eating:
        break
    sx, sy = eating[0], eating[1]
    time += eating[2]
    
    eat += 1
    num_fish -= 1
    if size == eat:
        size += 1
        eat = 0
    
    arr[sx][sy] = 0

print(time)