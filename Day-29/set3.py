# 1. Write a program to find the average of numbers in a list.
list = [4,6,8]
sum = 0
for i in list:
    sum+=i
print(sum/len(list))

# 2. Write a program to count how many times a number appears in a list.
list = [1, 2, 2, 3, 2]
count = 0
num = 2
for i in list:
    if i == num:
        count+=1
print(count)

#3. Write a program to get numbers greater than 5 from a list.
list = [2, 5, 7, 8]
for i in list:
    if i>5:
        print(i)

# 4. Write a program to replace all 0s with 1s in a list.
list = [0, 1, 0, 2]
list2 =[]
for i in list:
    if i == 0:
        list2.append(1)
    else:
        list2.append(i)

print(list2)

# 5. Write a program to print a list in reverse order.
list = [1, 2, 3]
print(list[::-1])

# 6. Write a program to merge two dictionaries.
data1, data2 = {'a': 1}, {'b': 2}
data1.update(data2)
print(data1)

# 7. Write a program to create a dictionary from two lists (one for keys and one for values).
key, value = ['a', 'b'], [1, 2]
data= dict(zip(key, value))
print(data)

# 8. Write a program to print all values from a dictionary.
data = {'x': 5, 'y': 10}
print(list(data.values()))

# 9. Write a program to get the length of a dictionary.
data = {'a': 10, 'b': 20, 'c': 30}
print(len(data))

# 10. Write a program to list all items in a dictionary as tuple
data = {'a': 1, 'b': 2}
print(list(data.items()))

# 11. Write a program to find the square of a number.
num = 6
print(num**2)

# 12. Write a program to find the sum of digits of a number.
num = 123
sum = 0
while num!=0:
    sum+=num%10
    num = num//10
print(sum)

#13. Write a program to find the smallest divisor of a number greater than 1.
num = 15
for i in range(2,num+1):
    if num%i == 0:
        print(i)
        break

# 14. Write a program to print the multiplication table of a number up to 10.
num = 3
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

# 15. Write a program to count the number of even digits in a number.
num = 2481
count = 0

while num!=0:
    digit = num%10
    if digit%2==0:
        count+=1
    num = num//10
print(count)
