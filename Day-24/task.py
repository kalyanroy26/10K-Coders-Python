
#TASK program to find nearest prime number

num = int(input("enter num: "))
num_2 = num #copy of number

#METHOD to check prime or not
def check_prime(num):
    fact = 0
    for i in range(1, num+1):
        if num%i == 0:
            fact+=1
    if fact == 2:
        return True
    else:
        return False

p_times = 1 #stores previous prime iterations
n_times = 1 #stores next prime iterations

previous_prime = 0
next_prime = 0

#code to check previous prime
while True:
    num-=1
    if check_prime(num):
        # print(f"previous prime is {num}")
        previous_prime = num
        break
    p_times+=1

#code to check next prime
while True:
    num_2+=1
    if check_prime(num_2):
        # print(f"next prime is {num_2}")
        next_prime = num_2
        break
    n_times+=1

#condition to check nearest prime using no of iterations
if p_times == n_times:
    print(f"nearest prime is {next_prime}")
elif p_times > n_times:
    print(f"nearest prime is {next_prime}")
else:
    print(f"nearest prime is {next_prime}")
