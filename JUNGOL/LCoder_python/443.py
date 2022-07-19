data = []

for i in range(10):
    name, score = map(str, input().split())
    data.append([name, int(score), i])
data.sort(key = lambda x: x[1], reverse=True)

score = 101
for i in range(10):
    if data[i][1] == score:
        data[i].append(rank)
    else:
        data[i].append(i + 1)
        rank = i + 1
    score = data[i][1]

data.sort(key = lambda x: x[2])
print("Name".rjust(4), end = "")
print("Score".rjust(6), end = "")
print("Rank".rjust(5), end = "")
print()
for d in data:
    print(f"{d[0].rjust(4)}{str(d[1]).rjust(6)}{str(d[3]).rjust(5)}")