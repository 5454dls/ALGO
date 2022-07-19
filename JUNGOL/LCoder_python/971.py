def function(n):
    for i in range(1, n + 1):
        count = i
        for j in range(n):
            print(count, end = " ")
            count += i
        print()

function(int(input()))