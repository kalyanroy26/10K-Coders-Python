# TASK 1  program to check whether string is valid or not

# if there is a will there is a way

string = input("Enter the string: ").upper()
valid = True
print(string)
for i in string:
    asc = ord(i)
    print(i, asc)
    if not (65<= asc <92 or asc == 32):
        valid = False
        break

if valid:
    print("Valid string")
else:
    print("Invalid string")

