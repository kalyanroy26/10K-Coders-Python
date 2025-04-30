#program to find sub string in string
# s = "helloworldheli"
# sub = "heli"
# present = False

# for i in range(len(s)):
#     if s[i]==sub[0]:
#         if sub == s[i:len(s)]:
#             present = True

# print(present)

# #shortest substring in string
# s = "programming"
# shortest = s

# for i in range(len(s)):
#     temp = ''
#     for j in range(i,len(s)):
#         if s[j] not in temp:
#             temp+=s[j]
#         else:
#             break
            
#     if len(temp) < len(shortest):
#         shortest = temp

# print(shortest)

# #longest sub string 
# s = "programming"
# longest = s

# for i in range(len(s)):
#     temp = ''
#     for j in range(i,len(s)):
#         if s[j] not in temp:
#             temp+=s[j]
#         else:
#             break
            
#     if len(temp) < len(longest):
#         longest = temp

# print(longest)

# longest palindrome
# s = "racecar"
# longest = ""

# for i in range(len(s)):
#     temp = ''
#     for j in range(i,len(s)):
#         temp+=s[j]
#         if temp == temp[::-1] and len(temp) > len(longest):
#             longest = temp

# print(longest)




