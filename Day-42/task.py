rows = 5
for i in range(rows,0,-1):
    res = ""
    for j in range(i,0,-1):
        res+=str(i)+" "
    print(res)

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

rows = 5
for i in range(rows,0,-1):
    res =" "
    for sp in range(rows-i):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *


rows = 5
mid = rows//2+1
for i in range(1,rows+1):
    res = ""
    for j in range(1,rows+1):
        if j==1 or j == rows or i == mid:
            res+="*"+" "
        else:
            res+="  "
    print(res)

# *       * 
# *       * 
# * * * * * 
# *       * 
# *       * 