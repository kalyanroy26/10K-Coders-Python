import random as r
import math as m

def generateOTP(k):
    otp = ""
    while len(otp)!=k:
        digit = m.floor(r.random()*10)
        if digit != 0:
            otp+=str(digit)

    return otp

size = int(input("enter OTP size: "))
print(generateOTP(size))


numbers = [1,2,3,4,5]
chances = 3

num = r.choice(numbers)
while chances!=0:
    guess = int(input("Guess the Number: "))
    print(num)
    if guess == num:
        print(f"you have guessed correct number {num} ")
        break
    elif chances == 0:
        print(f"no chances left, correct number {num} ")
    else:
        chances-=1
        print(f"try again, chances left {chances} ")