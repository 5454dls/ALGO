n_list = sorted(list(map(int, input().split())))

if n_list[0] == n_list[1] and n_list[1] == n_list[2]:
    print(10000 + (n_list[0] * 1000))
elif n_list[0] == n_list[1] or n_list[1] == n_list[2]:
    print(1000 + (n_list[1] * 100))
else:
    print(n_list[2] * 100)