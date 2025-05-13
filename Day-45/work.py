rows = 4
code = 97
for row in range(1,rows+1):
    res=""
    n = code + row - 1
    for col in range(1,row+1):
        res+=chr(n)+" "
        n+=rows-col
    print(res)

print("\n")

# a 
# b e 
# c f h 
# d g i j 

rows = 4
for row in range(1,rows+1):
    res=""
    n=row
    for col in range(1,row+1):
        res+=str(n)+" "
        n+=rows-col
    print(res)
print("\n")

# 1 
# 2 5 
# 3 6 8 
# 4 7 9 10 


rows = 5
for row in range(1,rows+1):
    res=""
    for sp in range(rows-row):
        res+="  "
    for col in range(1,row+1):
        res+=str(col)+" "
    for col in range(row-1,0,-1):
        res+=str(col)+" "
    print(res)
print("/n")

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1