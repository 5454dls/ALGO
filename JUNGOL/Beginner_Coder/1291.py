s, e = map(int, input().split())
i = 1
while True:
    if i == 10:
        break
    if 1 < s < 10 and 1 < e < 10:
        if s < e:
            for j in range(s, e + 1):
                result = str(j * i).rjust(2)
                print(f"{s} * {i} = {result}", end = "")
                print("   ", end = "")
        else:
            for j in range(s, e - 1, -1):
                result = str(j * i).rjust(2)
                print(f"{s} * {i} = {result}", end = "")
                print("   ", end = "")
        print()           
        i += 1
    else:
        print("INPUT ERROR!")
        s, e = map(int, input().split())