n = int(input())

divisorsList = []

for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
        divisorsList.append(i) 
        if ( (i**2) != n) : 
            divisorsList.append(n // i)

divisorsList.sort()

for r in divisorsList:
    print(r, end = " ")