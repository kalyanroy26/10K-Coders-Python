#p1

rows = 5
for row in range(1,rows+1):
    string = ""
    for col in range(1,rows+1):
        string+=str(row)+" "
    print(string)


#p2

rows = 5
for row in range(1,rows+1):
    string = ""
    for col in range(1,row+1):
        string+=str(row)+" "
    print(string)