list = [8,7,4,5,6,21,45,78,9,45,78,78]
max = list[0]
second_max = max

for i in list:
    if i>max:
        second_max = max
        max = i

print(max, second_max)
