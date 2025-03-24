# num_list = [22,33,66,99,121,19]

# for num in num_list:
#     if num%11 != 0:
#         print(num)


num_list = [4,5,6,3,0,2,5,9,9,15]
def count(list,num):
    count = 0
    for x in list:
        if x == num:
            count+=1
    return count

# num = int(input("enter number to count "))
# print("the number of times: ",count(num_list,num))

# function to copy unique elements to a list
unq_list = []

for num in num_list:
    if count(num_list,num) == 1:
        unq_list.append(num)

print(unq_list)


# LIST COMPREHENSION 
x = [num for num in num_list if num%2 == 0]
print(x)
