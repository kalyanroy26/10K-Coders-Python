# TASK-1 Program to find length of a number 

num = 62025348415
count = 0

while num!=0:
    num = num // 10
    count+=1

print("The length of number is ",count)

# TASK-2 program to find prime digit in a number

num = 6235567412

def check_prime(digit):
    fact = 0
    for i in range(1,digit+1):  
        if digit%i == 0: 
            fact+=1
    if fact == 2:
        return True
    else:
        return False
        
while num!=0:
    last_digit = num%10
    
    if check_prime(last_digit): #2
        print(last_digit, "is a prime digit from number")
   
    num = num//10


