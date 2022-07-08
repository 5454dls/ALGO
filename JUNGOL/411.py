def func(n):
    global count
    if n == 1:
        print(count)
    else:
        count += 1
        if n % 2 == 0:
            check = 2
        else:
            check = 3
        func(n // check)

n = int(input())
count = 0
func(n)