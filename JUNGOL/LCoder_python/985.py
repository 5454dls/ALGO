l = list(map(float, input().split()))
l.sort()

def func(l):
    tmp = list(str(l[2]))
    tmp[-2] = int(tmp[-2])
    tmp[-2] += 1
    tmp[-2] = str(tmp[-2])
    result = ""
    for n in tmp:
        result += n
    print(f"{int((l[2] // 1) + 1)} {int(l[0] // 1)} {int(round(l[1], 0))}")

func(l)