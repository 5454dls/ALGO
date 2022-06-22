num_list = []
while True:
    num = int(input())
    if num < 100:
        num_list.append(num)
    else:
        num_list.append(num)
        print(sum(num_list))
        print(round(sum(num_list) / len(num_list), 1))
        break