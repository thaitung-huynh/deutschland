line = input().split()

k =  int(line[0])
m =  int(line[1])

def modM(value):
    global m
    return ((value % m) * (value % m)) % m


a = [[0 for _ in range(9)] for _ in range(9)]

for i in range(k):
    lines = input().split()
    a[i][0] = int(lines[0])
    #for j in range(0, len(lines)):
     #   print(int(lines[j]))
    for j in range(1, a[i][0] + 1):
        a[i][j] = int(lines[j])

res = [[0 for _ in range(9)] for _ in range(9)]
for i in range(1, a[0][0] + 1):
    res[0][i] = modM(a[0][i])


for i in range(1, k):
    for j in range(1, a[i][0] + 1):
        for x in range(1, a[i - 1][0] + 1):
            if res[i][j] < (res[i - 1][x] + modM(a[i][j])) % m:
                res[i][j] = (res[i - 1][x] + modM(a[i][j])) % m
maxAns = 0

for i in range (1, a[k - 1][0] + 1):
    if maxAns < res[k - 1][i]:
        maxAns = res[k - 1][i]

print(maxAns)
