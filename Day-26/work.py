#TASK TO FIND LCM FROM 3 NUMBERS

num_1 = 15
num_2 = 50
num_3 = 70

big = max(num_1, num_2, num_3)
small = min(num_1, num_2, num_3)

if big%small == 0:
    print(f"{big} is LCM")
else:
    temp = big
    while True:
        if temp%num_1 == 0 and temp%num_2 == 0 and temp%num_3 == 0:
            print(f"{temp} is LCM")
            break
        temp+=big
        