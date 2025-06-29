# 1). Write a program to print the sum of the digits in the number

num = int(input("enter number: "))
sum = 0
while num!=0:
    sum+=num%10
    num = num//10
print(sum)

# 2). Write a program to print reverse of the given number.

num = int(input("enter number: "))
reverse = 0
while num!=0:
    digit = num%10
    reverse = digit+reverse*10
    num = num//10
print(reverse)

# 3). Write a program to print factorial of the number.  

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(3))

# 4). Write a program to print middle character(s) in the given string or number.

string = input("enter the string: ")
word_len = len(string)

if word_len%2 == 0:
    mid = word_len//2
    print(string[mid-1]+string[mid])
else:
    mid = word_len//2
    print(string[mid])

# 5). Write a program to check whether the sum of digits in the number except first digit and digit is equal to the sum of first digit and last digit of that number. If both the sums are equal then print equal otherwise print not equal

num = 75547
num = str(num)

if len(num)<3:
    print("not equal")
else:
    sum1 = int(num[0]) + int(num[-1])
    sum2 = sum(int(i) for i in num[1:-1])

    if sum1 == sum2:
        print("Equal")
    else:
        print("Not Equal")

# 6). Write a program to check whether the digits in-between the first and last digit are less than first and last digit, if yes then print true, otherwise print false
num = 84719
num = str(num)
length = len(num)
start = int(num[0])
end = int(num[-1])

if length%2==0:
    mid1 = int(num[length//2])
    mid2 = int(num[length//2-1])
    if (mid1 < start and mid1 < end) and (mid2 < start and mid2 < end):
        print(True)
    else:
        print(False)
else:
    mid = int(num[length//2])
    if mid < start and mid < end:
        print(True)
    else:
        print(False)


# Write a program to print the vowels in the given string in reverse order.
string = "HelloWorld"
vowels = "aeiouAEIOU"
v_l = []
for i in string:
    if i in vowels and i not in v_l:
        v_l.append(i)

print("".join(v_l))
        

# Write a program to print the vowels in the given string and repeated vowel should be printed only single time.
string = "JackspArrow"
vowels = "aeiouAEIOU"
v_l = []
for i in string:
    if i in vowels:
        v_l.append(i)

print("".join(v_l[::-1]))
        

# Write a program to convert all the upper case letters in the given string to lower case letter and vice versa.
string = "JohnWick"
new = ''
for i in string:
    code = ord(i)
    if 122>code>97:
        new+=chr(code-32)
    elif 90>code>65:
        new+=chr(code+32)
    else:
         new+=i
print(new)

    

#Write a program to print all the Upper case letters in the string in reverse order and then followed by the lower case letters .
string = "ClassLeader"
upper,lower = '',''
for i in string:
    code = ord(i)
    if 90>code>65:
        upper+=i
    else:
         lower+=i
print(upper[::-1]+lower)



# program to reverse a string without extra variable using recursion
def strReverse(s):
    if len(s)==0:
        return s    
    return strReverse(s[1:])+s[0]

print(strReverse('roy'))


# program to print numbers using recursion
def numPrint(n):
    if n == 0:
        return

    numPrint(n-1)
    print(n)

numPrint(5)


# program to find factorial using recursion
def factorial(n):
    if n == 1:
        return n
    
    return n * factorial(n-1) 

print(factorial(5))


# program to find sum of number from 1 to itself using recursion
def numSum(n):
    if n == 1:
        return n
    
    return n+numSum(n-1)

print(numSum(10))


# factorial using for loop
n = 5
fact = 1
for i in range(n,0,-1):
    fact*=i
print(fact)

# factorial using while 
n = 5
fact = 1
while n>0:
    fact*=n
    n-=1
print(fact)