n = int(input())
sq = n * n
str_n = str(n)
str_sq = str(sq)
if str_sq.endswith(str_n) :
    print("Automorphic Number")
else :
    print("Not an Automorphic Number")