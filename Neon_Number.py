n = int(input())
sq = n * n
str_sq = str(sq)
for i in range(len(str_sq)):
    sq_sum = 0
    for j in str_sq:
        sq_sum += int(j) 
if n == sq_sum :
    print("Neon Number")
else :
    print("Not Neon Number")