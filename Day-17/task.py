# TASK-1 Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid

para = """  
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        """

if len(list(para)) > 100:
    print("valid paragraph")
else:
    print("paragraph should be less than 100 words")


# TASK-2  take a input and count no of upper and lower case words

string = input("Enter the input with both upper and lower characters : ")
u_c = 0
l_c = 0

for i in string:
    if ord(i) >=65 and ord(i) <=92:
        u_c+=1
    elif ord(i) >= 97 and ord(i) <= 122:
        l_c+=1

print("Total Uppercase characters are ", u_c)
print("Total Lowercase characters are ", l_c)


