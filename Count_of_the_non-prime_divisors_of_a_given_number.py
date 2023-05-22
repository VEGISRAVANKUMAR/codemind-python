def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

n = int(input())
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

cnt = 0
for j in lst:
    if not isPrime(j):
        cnt += 1
        
print(cnt)