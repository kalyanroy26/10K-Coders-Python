#TASK - 1  Program to find number is in descending order

num = 987654321
previous = num%10 #saving last digit
dc_ord = True

while num!=0:
    last_digit = num%10
    if last_digit<previous: #comparing last digit should be less than previous digit
        dc_ord = False
        break
    previous = last_digit
    num = num//10

if dc_ord:
    print("Descending order")
else:
    print("Not Descending")
   

