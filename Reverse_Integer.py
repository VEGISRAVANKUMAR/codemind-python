n = int(input())
str_n = str(n)
if n > 0 :
    rev = str_n[::-1]
    print(int(rev))
else :
    rev = str_n[:0:-1]
    print(-int(rev))