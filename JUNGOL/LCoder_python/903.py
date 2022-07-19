l = []
for _ in range(10):
    l.append(input())
check = input()

for s in l:
    if s[-1] == check:
        print(s)