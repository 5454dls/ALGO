class student:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        data.append(self)

data = []
for i in range(5):
    n, h = map(str, input().split())
    i = student(n, int(h))
data.sort(key=lambda x: x.height)
print(data[0].name, data[0].height)