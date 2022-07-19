data = input().split()
tmp = []
answer = []

for s in data:
    if s == '(space)':
        answer.append(tmp)
        tmp = []
    elif s == data[-1]:
        tmp.append(s)
        answer.append(tmp)
    else:
        tmp.append(s)

for i in answer[::-1]:
    print(" ".join(i))