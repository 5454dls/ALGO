l = input().split()
check = list(set(l))
check.sort()
count = []

for c in check:
    count.append(l.count(c))

for i in range(len(count)):
    print(f"{check[i]} : {count[i]}")