def NumType(n):
    hasEven = False
    hasOdd = False
    
    for digit in n:
        if int(digit) % 2 == 0:
            hasEven = True
        else:
            hasOdd = True
    
    if hasEven and hasOdd:
        return "Mixed"
    elif hasEven:
        return "Even"
    else:
        return "Odd"

n = input()
res = NumType(n)
print(res)