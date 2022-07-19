SUM = 0
NUM = 0

while True:
    num = int(input())
    if 0 <= num <= 100:
        SUM += num
        NUM += 1
    else:
        if NUM == 0:
            NUM = 1
        print(f"sum : {SUM}")
        print(f"avg : {round(SUM / NUM, 1)}")
        break