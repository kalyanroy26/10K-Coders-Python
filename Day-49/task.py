# d = {'x': 10, 'y': 20}

# print(d.get('y',0))

# 2.	print all keys and values of the dictionary d = {'a': 1, 'b': 2} 
# d = {'a': 1, 'b': 2}
# for key in d:
#     print(key, d[key])

# 3.	Add a new key 'city' with value 'Delhi' to a dictionary ?

dict = {}
dict['city'] = 'delhi'
print(dict)

# 4.	d = {'a': 1, 'b': 2} and print all key-value pairs ?

d = {'a': 1, 'b': 2}
for key in d:
    print(key,": ", d[key])


# 5.	remove the key 'age' from d = {'name': 'Ajay', 'age': 22, 'gender': 'M'} and print the removed value ?

d = {'name': 'Ajay', 'age': 22, 'gender': 'M'}

print(d.pop('age'))