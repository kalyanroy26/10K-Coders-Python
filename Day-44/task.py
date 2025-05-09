#Diamond Pattern
rows = 5
for row in range(1,2*rows):
    res = ""
    space = rows-row if row<rows else row-rows
    cols = row if row<=rows else 2*rows-row

    for sp in range(1,space+1):
        res+=" "
    for col in range(1,cols+1):
        res+=str(col)+" "
    print(res)

#     1 
#    2 2 
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  6 6 6 6
#   7 7 7
#    8 8
#     9


#Hourglass Pattern

rows = 5
for row in range(1,2*rows):
    res = ""
    space = row-1 if row<rows else 2*rows-row-1 
    cols = rows-row+1 if row<=rows else row-rows+1

    for sp in range(1,space+1):
        res+=" "
    for col in range(1,cols+1):
        res+=str(col)+" "
    print(res)

# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3
#    1 2
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 