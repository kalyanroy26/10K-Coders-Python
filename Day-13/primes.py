def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count == 2:
        return True
    
prime_count = 0
sum_of_primes = 0
for num in range(1,101):
     if check_prime(num):
        print(num, end=" ")
        sum_of_primes+=num
        prime_count+=1
print('\n')
print("total primes are ", prime_count)
print("sum of primes from 1 to 100: ",sum_of_primes)

