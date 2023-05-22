n = int(input())
str_n = str(n)

set1 = set(str_n)
if len(str_n) == len(set1):
    print("Unique Number")
else:
    print("Not Unique Number")