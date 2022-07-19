l1 = set(list(map(int, input().split())))
l2 = set(list(map(int, input().split())))
l3 = set(list(map(int, input().split())))

print(f"Intersection: {l1 & l2 & l3}")
print(f"Union: {l1 | l2 | l3}")