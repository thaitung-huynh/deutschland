n = int(input())

a = set()
for i in range(n):
    a.add(int(input()))

m = int(input())
b = set()
for i in range(m):
    b.add(int(input()))

c = a - b
print(len(c))

