#even multiple  table 

num = int(input("enter the num: "))

for i in range(1,num+1):
    for j in range(1,21):
        if j%2 == 0:
            print(f"{i} X {j} = {i*j}")


#number of factors

count = 0
for i in range(1, num+1):
    if num%i == 0:
        count+=1

print(f"the number of factors for {count}")