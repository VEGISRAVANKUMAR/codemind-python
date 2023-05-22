import math

x, y, m = map(int, input().split())
print(int(math.pow(x,y) % m))