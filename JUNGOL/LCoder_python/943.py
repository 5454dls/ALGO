n = int(input())
for _ in range(n):
    name, rate, tier = map(str, input().split())
    if (float(rate) >= 60 and tier != "Bronze") or tier == "Platinum":
        print(f"[Gosu] {name}")