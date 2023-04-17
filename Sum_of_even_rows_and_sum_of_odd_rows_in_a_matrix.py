r,c = map(int, input().split())
mat=[]
for i in range(r):
    sub_list=map(int,input().split())
    mat.append(sub_list)
s=0    
d=0
for i in range(r):
    if i%2==0:
        s += sum(mat[i])
    elif i%2!=0:
        d += sum(mat[i])
        
    

print(s,d,end=' ')