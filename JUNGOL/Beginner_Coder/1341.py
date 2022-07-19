s, e = map(int, input().split())

if s < e:
    for i in range(s, e + 1):
        for j in range(1, 10, 3):
            r1 = str(j * i).rjust(2)
            r2 = str((j + 1) * i).rjust(2)
            r3 = str((j + 2) * i).rjust(2)
            print(f"{i} * {j} = {r1}   {i} * {j + 1} = {r2}   {i} * {j + 2} = {r3}")
        print()
else:
    for i in range(s, e - 1, -1):
        for j in range(1, 10, 3):
            r1 = str(j * i).rjust(2)
            r2 = str((j + 1) * i).rjust(2)
            r3 = str((j + 2) * i).rjust(2)
            print(f"{i} * {j} = {r1}   {i} * {j + 1} = {r2}   {i} * {j + 2} = {r3}")
        print()       