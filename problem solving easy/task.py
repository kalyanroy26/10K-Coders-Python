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

# 5). Write a program to check whether the sum of digits in the number except

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
