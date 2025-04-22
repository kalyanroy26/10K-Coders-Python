list1 = [2, 3, 6, 6, 5]

list1 = list(set(list1))

list1.sort(reverse=True)

if len(list1)>1:
    second_max = list1[1]
    max = list1[0]
print(max, second_max)



