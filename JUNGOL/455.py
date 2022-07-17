s = input().split()
s.sort(key = lambda x:len(x), reverse = True)

count = 0
for a in s:
    count += len(a)
    count += 1
print(count - 1)
print(s[0], end = " ")
for a in s[1:]:
    if len(a) == len(s[0]):
        print(a, end = " ")
    else:
        break