data = input().split()
sep = input()
tmp = []
answer = []

for s in data:
    if s == sep:
        print(" ".join(tmp))
        tmp = []
    elif s == data[-1]:
        tmp.append(s)
        print(" ".join(tmp))
    else:
        tmp.append(s)
