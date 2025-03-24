#1. odd or even program
num = int(input("enter the number: "))

if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

#2. larger number
num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))


if num1 > num2:
    print("num1 is greater")
elif num2 >num1:
    print("num2 is greater")
else:
    print("Both are equal")

#3. positive or negative

if num >0:
    print("positive Number")
elif num<0:
    print("Negative Number")
else:
    print("Zero")

#4. age access

age = int(input("Enter Your Age: "))

if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#5. student marks

marks = int(input("Enter your marks: "))

if marks>100:
    print("wrong input")
elif marks>=40:
    print("Pass")
else:
    print("Fail")

