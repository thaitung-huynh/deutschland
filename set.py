n = int(input())

a = {int(val) for val in input().split(" ")}


m = int(input())
b = {int(val) for val in input().split(" ")}


c = a - b
print(len(c))

