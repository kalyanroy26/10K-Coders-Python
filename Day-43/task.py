rows = 5
for row in range(1,rows+1):
    res=""
    for col in range(rows,0,-1):
        if row == col or row == 1 or row==rows:
            res+="*"+" "
        else:
            res+="  "
    print(res)
print("\n")

# * * * * * 
#       *   
#     *
#   *
# * * * * *

rows = 5
for row in range(1,rows+1):
    res=""
    for col in range(1,rows+1):
        if row == col or col == 1 or col==rows:
            res+="*"+" "
        else:
            res+="  "
    print(res)
print("\n")

# *       * 
# * *     * 
# *   *   *
# *     * *
# *       *

rows = 10
mid = rows//2+1
for row in range(1,rows+1):
    res=""
    for col in range(1,rows+1):
        if row == 1 or col == 1 or row == mid or (row==col and row+col>mid and row>mid) or (col == rows and row<mid):
            res+="*"+" "
        else:
            res+="  "
    print(res)
print("\n")

# * * * * * 
# *       * 
# * * * * *
# *     *  
# *       *

rows = 5
mid = rows//2 +1
for row in range(1,rows+1):
    res=""
    for col in range(1,rows+1):
        if row == 1 or col == 1 or col == rows or row == mid:
            res+="*"+" "
        else:
            res+="  "
    print(res)

# * * * * *
# *       *
# * * * * *
# *       *
# *       *