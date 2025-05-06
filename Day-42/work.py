#pattern 1
# rows = 5
# for i in range(1,rows+1):
#     res = ""
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


#pattern 2
# rows = 5
# for i in range(rows+1):
#     res = ""
#     for j in range(1,i+1):
#         res+=str(j)+" "
#     print(res)

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#pattern 3
# rows = 5
# for i in range(rows,0,-1):
#     res = ""
#     for j in range(i,0,-1):
#         res+=str(j)+" "
#     print(res)

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1
# 2 1
# 1

#pattern 4
# rows = 5
# for i in range(rows,0,-1):
#     res = ""
#     for sp in range(rows-i):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

# * * * * * 
#  * * * * 
#   * * *
#    * *
#     *


#pattern 5
# rows = 5
# for i in range(1,rows+1):
#     res = ""
#     for sp in range(rows-i):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

#pattern 5
# rows = 7
# mid = rows//2 +1
# for i in range(1,rows+1):
#     res =" "
#     for j in range(rows-2):
#         if i ==1 or i==rows or j ==0 or i == mid:
#             res+="*"+" "
#     print(res)


#  * * * * * 
#  *
#  * 
#  * * * * *
#  *
#  *
#  * * * * *

# rows = 5
# for i in range(1,rows+1):
#     res = ""
#     for j in range(1,rows+1):
#         if i==j or i+j == rows+1:
#             res+="*"+" "
#         else:
#             res+="  "
#     print(res)

# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 

# rows = 5
# mid = rows//2+1
# for i in range(1,rows+1):
#     res = ""
#     for j in range(1,rows+1):
#         if i==1 or i == rows or j == mid:
#             res+="*"+" "
#         else:
#             res+="  "
#     print(res)

# * * * * * 
#     *     
#     *     
#     *     
# * * * * *

# rows = 5
# mid = rows//2+1
# for i in range(1,rows+1):
#     res = ""
#     for j in range(1,rows+1):
#         if j==1 or j == rows or i == mid:
#             res+="*"+" "
#         else:
#             res+="  "
#     print(res)

# *       * 
# *       * 
# * * * * *
# *       *
# *       *


# rows = 5
# mid = rows//2+1
# for row in range(1,rows+1):
#     res = ""
#     for col in range(1,rows+1):
#         if row == 1 or row == rows or row == mid or (row==2 and col == row-1) or (row==4 and col == rows):
#             res+="*"+" "
#         else:
#             res+="  "
#     print(res)

# * * * * * 
# *
# * * * * * 
#         * 
# * * * * *

