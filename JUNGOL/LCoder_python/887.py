data = input().split()
check = int(data[1])
l = len(data[0])

for _ in range(int(data[2])):
    print(data[0][check : ] + data[0][ : check])
    check += int(data[1])
    if check > l:
        check -= l