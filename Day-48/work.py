
# matrix = [
#     [1,0,0],
#     [0,1,0],
#     [0,0,1]
# ]

# is_unity = True
# is_square = False

# for sub in matrix:
#     if len(sub)==len(matrix):
#         is_square = True

# if is_square:
#     i=0
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i==j and matrix[i][j]!=1:
#                 is_unity = False
#                 break
#             elif i!=j and matrix[i][j]!=0:
#                 is_unity = False
#                 break
# else:
#     print("not a square matrix")


# if is_unity:
#     print("matrix is unity")

            
      
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 

# transpose = []

# for i in range(len(matrix)):
#     row = []
#     for j in range(len(matrix[0])):
#         row.append(matrix[j][i])
#     transpose.append(row)
# print(transpose)
            