a = int(input())
b = int(input())
for i in range(a, b+1):
    str_n = str(i)
    if len(str_n) == 1:
        print(i, end=" ")
    elif i % 10 == 0:
        continue
    else:
        is_self_dividing = True
        for j in range(len(str_n)):
            if int(str_n[j]) == 0 or i % int(str_n[j]) != 0:
                is_self_dividing = False
                break
        if is_self_dividing:
            print(i, end=" ")