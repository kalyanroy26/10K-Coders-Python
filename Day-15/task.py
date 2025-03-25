# TASK-1 Practise string methods

string = '      10K Coders institute    '

print(string.upper())
print(string.lower())
print(string.count('t'))
print(string.find('coders'))
print(string.replace('institute','school'))
print(string.lstrip())
print(string.strip())



# TASK-2 Program to convert first occurence of a letter to uppercase

new_string =''
ind=0

for i in range(len(string)):
    if string[i] == 'i':
        ind = i
        break


for i in range(len(string)):
    if i == ind:
        new_string+='I'
    else:
        new_string+=string[i]

print(string)
print(new_string)