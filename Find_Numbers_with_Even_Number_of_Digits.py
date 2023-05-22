def findNumbers(nums):
    cnt = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            cnt += 1
    return cnt

n = int(input())
nums = list(map(int, input().split()))

res = findNumbers(nums)
print(res)
