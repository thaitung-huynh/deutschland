n = int(input("Input N: "))
a = []

for i in range(n):
    a.append(int(input(f"a [{i}]")))

sum = 0
for value in a:
    sum += value


print(sum)

