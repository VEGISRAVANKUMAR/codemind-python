n, m = map(int, input().split())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
    s = 0
    for i in mat:
        for j in i:
            s += j
print(s)