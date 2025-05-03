
rows =5
code = 97
for row in range(1,rows+1):
    if row == 1:
        print(chr(code))
        code+=1
    elif row == 2:
        print(chr(code),chr(code+1))
        code+=2
    elif row == 3:
        print(chr(code)," ",chr(code+2))
        code+=3
    elif row == 4:
        print(chr(code)," "," ",chr(code+3))
        code+=4
    elif row == 5:
        print(chr(code),chr(code+1),chr(code+2),chr(code+3))