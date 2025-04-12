# 1. Sum of elements in a list
list = [4,7,2]
sum = 0
for ele in list:
    sum+=ele
print(sum)

# 2. Find the largest number in a list
list = [3,10,6]
max = list[0]
for ele in list:
    if ele>max:
        max = ele
print(max)

# 3. Count even numbers in a list
count = 0
list = [1,2,3,4,5,6,7,8]

for ele in list:
    if ele%2==0:
        count+=1
print(count)

# 4. Remove duplicates from a list
list_1 = [1,2,3,4,2,2,1,2,1,5,6,7]
print(list(set(list_1)))

#5. Find the second largest number
list = [1,2,3,4,5,6,7,8]
list.sort()
print(list[-2])

# 6. Count word occurrences in a sentence
str = "apple banana apple"
new_str = str.split(" ")
word_count = {}
count = 0
for i in new_str:
    word_count[i] = word_count.get(i,0)+1
print(word_count)

#7. Update value of a key in a dictionary
data = {
    "a":5,
    "b":2
}
for key in data:
    if key == 'a':
        data[key] = 10
        break
print(data)

# 8. Check if a key exists in a dictionary
data = {
    "x":5,
    "y":2
}

for key in data:
    if key == 'x':
        print(True)

# 9. Print only dictionary keys  
data = {'name': 'Ava', 'age': 21}
print(list(data.keys()))

# 10. Add new key-value if key doesn't exist
data = {
    "x":5,
    "y":2
}
key = 'z'
if key not in data:
    data[key] = 10
print(data)

# 11. Check if a number is even or odd
num = 7
if num%2 == 0:
    print("even")
else:
    print("odd")

# 12. Find factorial of a number
num = 5
def fact(n):
  if n == 1:
       return n
  else:
       return n*fact(n-1)
print(fact(num))

# 13. Check if a number is prime
num = 5
def check_prime(n):
    fact = 0
    for i in range(2,n):
        if n%i == 0:
            fact+=1
            break
    if fact == 0:
        return "Prime"
    else:
        return "Not a Prime"
print(check_prime(num))

# 14. Reverse digits of a number
num = 1234
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10
print(rev)

# 15. Count digits in a number
num = 12345
count = 0
while num!=0:
    digit = num%10
    count+=1
    num = num//10
print(count)