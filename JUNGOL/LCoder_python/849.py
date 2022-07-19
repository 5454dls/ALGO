for i in range(2, 5):
    for j in range(1, 6):
        result = str(i * j).rjust(3)
        print(f"{i} * {j} ={result}  ", end = ' ')
    print()