num = 14689
previous = num%10 #saving last digit
asc_ord = True

while num!=0:
    last_digit = num%10
    if previous<last_digit:
        asc_ord = False
        break
    previous = last_digit
    num = num//10

if asc_ord:
    print("Ascending order")
else:
    print("Not Ascending")
   

