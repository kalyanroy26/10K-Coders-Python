# TASK-1 program to separate prime and non prime numbers into separate list

num_list = [2,3,4,5,6,7,8,9,10,11,12,13,15,17,14,19,21,23,27,31]
prime_list = []
non_prime_list = []

def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count == 2:
        prime_list.append(num)
    else:
        non_prime_list.append(num)


for num in num_list:
    check_prime(num)

print("prime list: ",prime_list)
print("non prime list: ", non_prime_list)


# TASK-2  create mydetails dictionary and perform dictionary methods

my_details = {
    "name": "kalyan maharajulu",
    "age": 23,
    "education": "Bachelors in CSE",
    "skills": ['HTML','CSS','javascript','react.js','node.js','Git', 'postman'],
    "batch": "37R"
}

print(my_details.get("name"),'\n')

print(my_details.keys())

print(my_details.values(),'\n')

print(my_details.items(),'\n')

print(len(my_details['skills']),'\n')

print(my_details.clear())