#TASK -1 program to separate odd & even elements from list 

num = [2,4,3,1,5,6,7,8,9,10]
even = []
odd = []

for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.extend(odd)

print(even)



# #TASK -2 program to separate unq elements from last and add "*" at EOL 

num = [2,4,3,2,1,2,4,5,1]
unq =[]
count = 0 
for i in num:
    if i not in unq:
        unq.append(i)
    else:
        count+=1
        
for i in range(count):
    unq.append("*")

print(unq)

# #TASK -3 program to separate unq elements from last and replace with "*"  

num = [2,4,3,2,1,2,4,5,1]
unq =[]
for i in num:
    if i not in unq:
        unq.append(i)
    else:
        unq.append("*")
        
print(unq)