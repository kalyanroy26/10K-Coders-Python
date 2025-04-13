# 1. Multiply all elements in a list
list = [2, 3, 4]

total = 1
for i in list:
    total *= i
print(total)

# Find minimum value in a list
list = [8, 3, 5]

min = list[0]
for i in list:
    if i < min:
        min = i
print(min)

# 3. Find count of odd numbers in a list
list = [2, 5, 7, 8]
count = 0
for i in list:
    if i%2 != 0:
        count+=1
print(count) 

# 4. Find difference between max and min
list = [4, 7, 2, 9]
min = list[0]
max = list[0] 
for i in list:
    if i > max:
        max = i
    if i < min:
        min = i
print(max-min) 

# 5. Sum of only positive numbers
list = [-1, 3, 5, -2]
sum = 0
for i in list:
    if i > 0:
        sum+=i
print(sum) 

# 6. Get keys with even values from dict
data = {'a': 2, 'b': 3, 'c': 4}
list = [key for key in data if data[key]%2==0 ]
print(list)

# 7. Invert dictionary (keys become values)
data = {'x': 1, 'y': 2}
new_data = {}
for key in data:
    new_data[data[key]] = key
print(new_data)

# 8. Check if two dictionaries are equal
dict1 , dict2 = {'a': 1} , {'a': 1}
print(dict1==dict2)

# 9. Sum all values in dictionary
data = {'a': 5, 'b': 10}
sum = 0
for i in data :
    sum+=data[i]
print(sum)

# 10. List all values greater than 10
data = {'a': 8, 'b': 12, 'c': 15}
list = [data[key] for key in data if data[key]>10]
print(list)

# 11. Check if number is positive, negative or zero
num = -4
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# 12. Generate first 5 even numbers
count = 5
num = 0
list = []
while count!=0:
    num+=1 
    if num%2 == 0:
        list.append(num)
        count -=1 
print(list)

# 13. Find cube of a number
num = 3
print(num**3)

# 14. Check if number is multiple of 7
num = 21
if num%7 == 0:
    print("yes")
else:
    print("no")

# 15. Convert number to string and reverse it
num = 123 
print(str(num[::-1]))