# while True:
#     s = input()
#     if s == 'END':
#         break
#     else:
#         print(s[::-1])

answer = []
while True:
    s = input()
    if s == 'END':
        break
    else:
        answer.append(s[::-1])

for data in answer:
    print(data)