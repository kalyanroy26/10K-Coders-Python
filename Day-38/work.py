# shortest palindrome
s = "racecar"
shortest = s

for i in range(len(s)):
    temp = ''
    for j in range(i,len(s)):
        temp+=s[j]
        if temp == temp[::-1] and len(temp) < len(shortest):
            if len(temp)>2:
                shortest = temp

print(shortest)