numbers = [2,4,5,7,8,9,10,12]

search = int(input("enter number in the list want  to replace: "))
replace = int(input("enter the replacement number:"))
search_index = numbers.index(search) 

for num in numbers:
    if search == num:
        numbers.remove(search)
        numbers.insert(search_index,replace)
    
print(numbers)


# dup = []
# num = 7
# replace = 6
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         dup.append(replace)
#     else:
#         dup.append(numbers[i])
# print(numbers)

# print(dup)