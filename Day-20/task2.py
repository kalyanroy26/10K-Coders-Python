#TASK - 2  Program to find count and its positions of a digit in number

num = 6302525995
temp = num
length = 0
digit = 5  # enter digit to find its pos
pos = []
count = 0
is_ex = False

while num!=0:       #Finding length
    num = num//10
    length+=1

while temp!=0:
    last_digit = temp%10
    if last_digit == digit:
        is_ex = True
        pos.append(length)
        count+=1
    
    length-=1
    temp = temp//10

if is_ex:
    pos.sort()
    print("positions of digit: ",pos)
    print("count of digit in number: ",count)
else:
    print("Doesn't Exist")



