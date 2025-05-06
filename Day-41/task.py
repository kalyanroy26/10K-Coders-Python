
rows =5

for r in range(1,rows+1):
    res=""
    for c in range(1,rows+1):
        if r==1 or r == rows or c == 1 or c == rows or c== (rows//2)+1 and r == (rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
        

    print(res)
    