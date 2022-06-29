target = input().strip()
answer = 'Pennsylvania'
flag = 0

for i in range(len(answer) - len(target) + 1):
    if target[0] == answer[i]:
        for j in range(len(target)):
            if target[j] != answer[i + j]:
                print(j)
                break
            elif j == (len(target) - 1):
                flag = 1
    
    if flag:
        break

if flag:
    print("True")
else:
    print("False")