list = [[1,2,3,16],[10,15,12],[4,5,6],[7,8,9]]

# for i in range(len(list)):
#     for j in range(len(list[i])):
#         print(list[i][j],end=" ")

#max elements in sub list
sub_list=[]
for i in list:
    sub_list.append(max(i))
print(sub_list)
