rows=5
for row in range(1,rows+1):
    s = ''
    for col in range(1,row+1):
        s+=str(col)+" "
    print(s)
