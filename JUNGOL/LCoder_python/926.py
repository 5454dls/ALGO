s1 = input()
l1_1 = list(map(int, input().split()))
l1_2 = list(map(int, input().split()))
s2 = input()
l2_1 = list(map(int, input().split()))
l2_2 = list(map(int, input().split()))

for i in range(4):
    print(l1_1[i] * l2_1[i], end = " ")
print()
for i in range(4):
    print(l1_2[i] * l2_2[i], end = " ")