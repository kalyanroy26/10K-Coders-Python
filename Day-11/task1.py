num_list = [2,3,4,5,6,7,9,8,11,13,15,17,19,21,23,27]
prime_list = []
count = 0

#function to check prime number
def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count == 2:
        return True


#passing each value from list to check whether they are prime or not
for num in num_list:
    if check_prime(num) == True:
        prime_list.append(num)


print("prime list is ",prime_list)

