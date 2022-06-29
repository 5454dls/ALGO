data = []

for _ in range(3):
    s = input()
    data.append(s)

correct = sorted(data)       

if data == correct:
    print("YES")
else:
    print("NO")