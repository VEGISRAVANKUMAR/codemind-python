a = int(input())
b = int(input())

def is_pal(n):
    return str(n) == str(n)[::-1]

for i in range(a, b + 1):
    if is_pal(i):
        print(i, end = " ")