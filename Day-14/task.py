# TASK-1 program to check voter eligibility
voters_list = [
    {
        "name":"kalyan",
        "age": 19,
        "citizen": 'indian',
    },
    {
        "name":"Teja",
        "age": 21,
        "citizen": 'indian',
    },
    {
        "name":"praveen",
        "age": 21,
        "citizen": 'pakistan',
    }
]

for i in range(len(voters_list)):
    if voters_list[i]['age'] > 18 and voters_list[i]['citizen']=='indian':
        voters_list[i]['eligible'] = True
        print(voters_list[i])
        


# TASK-2 Program to find unique elements in tuple

my_tuple = (2,1,4,5,6,2,3,7,9,10,5,11,15,16,2,11,20,25,29)
unique_list = []    # empty list

def check_unique(ele,my_tuple):  # function to check element is unique or not 
    count = 0
    for i in range(0,len(my_tuple)):
        if my_tuple[i] == ele: # checking 
            count+=1
    if count == 1:   # element should occur only once 
        return True
    else:
        return False
    
        

for ele in my_tuple:
    if check_unique(ele,my_tuple): # checking whether element is unique or not 
        unique_list.append(ele)


print(my_tuple)
print(tuple(unique_list))