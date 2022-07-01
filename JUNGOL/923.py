l = input().split()
check = []
count = []

for n in l:
    if len(n) == 2:
        check.append(n[0])
    else:
        check.append("0")

check = list(set(check))
check.sort()

for c in check:
    tmp = 0
    for s in l:
        if s[0] == c:
            tmp += 1
    count.append(tmp)

for i in range(len(count)):
    print(f"{check[i]} : {count[i]}")