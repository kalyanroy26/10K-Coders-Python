num = int(input("enter the num: "))

fact = 0
for i in range(2,num-1):
    if num%i==0:
        fact+=1
    
if fact>0:
    print("its not a prime")
else:
    print("prime number")
