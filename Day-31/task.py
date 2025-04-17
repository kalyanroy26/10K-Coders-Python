# PROGRAM TO CONVERT FIRST LETTER OF A WORD TO UPPERCASE
str = "teja uday"
str = str.split(" ")
new = ""

for i in str:
    new+=i.title()+" "

print(new)

#PROGRAM TO PRINT CHARACTER WITH HIGHEST OCCURENCES
sentence = "dont trouble the trouble"
char_count = {}
for i in sentence:
    char_count[i] = char_count.get(i,0)+1

c=0
max = ''

for key in char_count:
    if char_count[key]>c:
        c=char_count[key]
        max = key

print(max,c)
