
num = int(input("enter the num: "))

prime_not_found = True
loop_times = 0
while prime_not_found:
    num+=1
    count = 0
    loop_times+=1
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count==2:
        prime_not_found = False
        print("Next Prime is ",num)
        print("number of loops: ", loop_times)






