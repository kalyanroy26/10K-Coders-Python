num = int(input("enter the num: "))
no_of_primes = 0

prime_not_found = True
while prime_not_found:
    num+=1
    count = 0
    
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count==2:
        no_of_primes+=1
        
    if no_of_primes==2:
        print(num)
        break