list1 = 2
list2 = 2
list3 = 2

n = 2

num = [[i,j,k] for i in range(list1+1) for j in range(list2+1) for k in range(list3+1)  if i+j+k==n]

print(num)