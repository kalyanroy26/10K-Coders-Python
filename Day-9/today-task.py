num = int(input("enter the number "))

#Program to not print multiples of 3  task-1
for i in range(1,101):
    if i%3 == 0:
        continue
    else:
        print(i)


#Program to find second prime task-2

no_of_primes = 0

def next_prime(num):
    prime_not_found = True
    while prime_not_found:
        num+=1
        count = 0
        for i in range(1,num+1):
            if num%i == 0:
                count+=1
        if count == 2:
            return num
        
while True:
    num = next_prime(num)
    no_of_primes+=1

    if no_of_primes == 10:
        print("Second Prime: ",num)
        break
