#TASK 1 FIND MISSING NUMBER IN A LIST
num = [2,3,4,6,8,10]

for i in range(1,max(num)):
    if i not in num:
        print(f"{i} is missing number.")

#TASK 2 Take a dictionary with salaries and Find percentage of the salaries
data = {
    'kalyan': 700000,
    'naveen': 1000000
}

total = 0

for key in data:
    total+=data[key]

for key in data:
    perc = data[key]/total *100
    print(f"{key} salary percentage: {perc.__ceil__()}%")
