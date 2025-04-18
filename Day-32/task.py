#Program to print the count of  number of Fibonacci numbers in between of 0 to 500 
a,b = 0,1
count=0 #counter to count fibonacci numbers 
while a<=500:
    print(a,end=" ") #to print initial starting 0 fibonacci series
    a,b = b,a+b  #swapping a with b and b with a+b
    count+=1


print("\n")
print("count: ", count)