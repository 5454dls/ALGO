N, K = map(int, input().split())

count = 0
check = 1
while True:
    if check > N:
        result = 0
        break
    if count == K:
        result = check - 1
        break
    if N % check == 0:
        count += 1
    check += 1
print(result)