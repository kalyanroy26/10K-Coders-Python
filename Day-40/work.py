rows = 5
code =97
for row in range(rows):
    res = ""
    for col in range(1,row+1):
        res+=chr(code)+" "
    print(res)
print('\n')


rows = 5
for i in range(1,rows+1):
    res = ""
    for j in range(1,i+1):
        if i==j or i==rows or j == 1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
print('\n')


rows = 5
for i in range(1,rows+1):
    res = ""
    for j in range(1,i+1):
        if i==1 or i==rows or j == rows or j==1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
print('\n')
    
