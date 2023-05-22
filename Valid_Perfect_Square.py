def isPerfectSquare(n):
    if n < 0:
        return False
    if n == 0:
        return True

    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n


t = int(input())

for _ in range(t):
    n = int(input())
    print(isPerfectSquare(n))
