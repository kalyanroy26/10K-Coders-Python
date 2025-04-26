# program to rotate a string or list
# string = input("enter string to rotate: ")
string = [2,5,6,7,8,9]
rotations = int(input("enter rotations: "))

rotations = rotations%len(string)


for i in range(rotations):
    print(i)
    string = string[1:len(string)]+string[0:1]
print(string)