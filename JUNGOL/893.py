A = input().split()
B, C = input().split()
l = len(B)
check = 0

for i in range(len(A)):
    if A[i][:l] == B:
        check += 1
        A[i] = C + A[i][l:]

print(check)
print(" ".join(A))