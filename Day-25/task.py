list = [[1,2,3,16],[10,15,12],[4,5,6],[7,8,9]]

#max element in sub list
max_sub_list=[]
for i in list:
    max_sub_list.append(max(i))
print("max: ",max(max_sub_list))

#min element in sub list
min_sub_list=[]
for i in list:
    min_sub_list.append(min(i))
print("minimum: ",min(min_sub_list))