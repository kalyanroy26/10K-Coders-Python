# list = [6,4,6,2,1,3,4]

# def ele_count(arr):
#     char_count = {}
#     for ele in arr:
#         char_count[ele] = char_count.get(ele, 0)+1

#     return char_count

# list_count = ele_count(list)

# print(list_count)

# max = 0
# ele = 0
# for key in list_count:
#     if list_count[key]>max:
#         max = list_count[key]
#         ele = key

# print("max", ele)


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# car = 5
# people = 26

# no_of_cars = people//car

# if people%car!=0:
#     no_of_cars +=1 

# print(no_of_cars)



# list = [1,2,3,4,5,6,7,8,9]
# newList = []
# sub = []

# for ele in list:
#     sub.append(ele)

#     if len(sub)==3:
#         newList.append(sub)
#         sub = []

# print(newList)



#anti diagonal matrix[i][n-1-i]
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sub = []        
for i in range(len(matrix)):
    sub.append(matrix[i][len(matrix)-1-i]) 

print(sub)


#find given matrix is square or not 

def isSquare(m):
    flag = False
    for sub in m:
        if len(sub)!=len(m):
            flag =  False
            break
        else:
            flag = True
    return flag

print(isSquare(matrix))



#non diagonal elements in a matrix
def non_diagonal(m):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i!=j:
                res.append(matrix[i][j])
    return res

print(non_diagonal(matrix))   



# transpose of a matrix
def transpose(m):
    matrix = []

    for i in range(len(m)):
        sub = []
        for j in range(len(m)):
            sub.append(m[j][i])
        matrix.append(sub)
    return matrix

print(transpose(matrix))
