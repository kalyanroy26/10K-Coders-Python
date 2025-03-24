# TASK-1 program to find whether the first and last element of the list is even 

num_list = [4,5,6,3,0,2,5,9,9,15]

def check_even(num_list):
    if num_list[0]%2 == 0 and num_list[-1]%2 == 0:
        return True
    else:
        return False

print(check_even(num_list))


# TASK-2 program to duplicate count function 

def count(list,num):
    count = 0
    for x in list:
        if x == num:
            count+=1
    return count

num = int(input("enter number to count "))
print("the number of times: ",count(num_list,num))


# TASK-3 program to copy only prime numbers from a list

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

