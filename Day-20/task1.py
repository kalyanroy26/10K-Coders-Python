num = 6302525
temp = num
length = 0
pos = 2

while num!=0:       #Finding length
    num = num//10
    length+=1

if pos<=length:
    while temp!=0: 
        digit = temp%10 
        if length == pos: 
            print(digit)
            break

        length-=1 
        temp = temp//10 

else:
    print("not enough positions")

