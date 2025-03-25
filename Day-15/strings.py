string = "institute".lower()
i = string.find('i')
new_string = ''

new_string = list(string)
new_string[i] = 'I'
string = "".join(new_string)
print(string)

