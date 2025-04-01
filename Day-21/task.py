#TASK program to find user given nth prime with callback functions

num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))

#function to check prime
def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count == 2:
        return True
    
#function which returns nth prime 
def nth_prime(n): 
    prime_count = 0  #counts prime numbers from 1 
    num = 1 #initial number to start prime count
    while prime_count<n: #while prime count is less than user input
        num+=1
        if check_prime(num): #calling function to check prime or not **CALLBACK**
            prime_count+=1
    return num

#function call
print(nth_prime(num_1))
print(nth_prime(num_2))

