# n개 중 k개(조합, 부분집합)
def com(level, s):
    if level == k:
        print(c)
        return
    else:
        # n - k + 1 = 처음 고를 때 몇 까지 갈 수 있는가?
        for i in range(s, n - k + level + 1):
            c[level] = arr[i]
            # 또 다른 세상이 정의 된다.
            # i를 이미 채웠기 때문에 다음 자리는 i보다 큰 수를 채울 수 있다.
            com(level + 1, i + 1)


n = 5
k = 3

arr = list(range(n))
c = [0] * k
# 최초의 세상
com(0, 0)