
# TASK-1 program to perform user defined count function 
numbers = [2,4,6,8,1,4,2,5,4,1,4,4,6,6,6,6,6,6,6,6,6,6,6]
dupe = []

search = int(input("enter number to find no of times: "))

count = 0
for num in numbers:
    if search == num:
        count+=1
    
print("no of times repeated: ",count)

# TASK-2 program to copy list to new list

for i in range(len(numbers)):
    dupe.append(numbers[i])

print("numbers: ", numbers)
print("dupe: ",dupe)