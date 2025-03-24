num = int(input("enter the number "))
val = 0


def next_prime(num):
    prime_not_found = True
    while prime_not_found:
        num+=1
        count = 0
        for i in range(1,num+1):
            if num%i == 0:
                count+=1
        if count == 2:
            break
            prime_not_found=False

    return num
        

while val<2:
    first_prime = next_prime(num)
    second_prime = next_prime(first_prime)
    print("primes: ",second_prime)
    val+=1
