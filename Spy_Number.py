n = int(input())
str_n = str(n)
for i in range (len(str_n)) :
    sums = 0
    pros = 1
    for j in str_n :
        sums += int(j)
        pros *= int(j)
        
if sums == pros :
    print("Spy Number")
else :
    print("Not Spy Number")