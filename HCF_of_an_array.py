import math

n = int(input())
arr = list(map(int, input().split()))

hcf = arr[0]
for i in range(1, n):
    hcf = math.gcd(hcf, arr[i])

print(hcf)