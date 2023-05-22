for _ in range(int(input())):
    s = input()
    
    flag = False
    for i in s:
        if i.isdigit():
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")