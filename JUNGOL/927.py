score = []
for _ in range(5):
    score.append(list(map(int, input().split())))

count = 0
for i in range(5):
    if sum(score[i]) >= 320:
        print("pass")
        count += 1
    else:
        print("fail")
        
print(f"Successful : {count}")