# program to rotate a string or list
string = input("enter string to rotate: ")
string = [2,5,6,7,8,9]
rotations = int(input("enter rotations: "))

rotations = rotations%len(string)


for i in range(rotations):
    print(i)
    string = string[1:len(string)]+string[0:1]
print(string)

#Run-Length Encoding for Strings
string = 'aaaabbcccca'
new = ''
i = 0
count = 1

while i<len(string):
    
    if i <len(string)-1 and string[i] == string[i+1]:
        count+=1
    else:
        new += string[i] +str(count)
        count=1
    i+=1

print(new)
