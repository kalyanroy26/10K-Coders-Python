# rows = 5

# for row in range(1,rows+1):
#     res = ""
#     for col in range(1,rows+1):
#         res+=str(col)+" "
#     print(res)


# rows = 5

# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if col==1 or col==rows or col==row:
#             res+="*"+" "
#         else:
#             res+="  "
#     print(res)


# rows = 5

# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if row==1 or row==rows or col+row==rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)


# rows = 5

# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if col==1 or col==rows or row==rows//2+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# rows=5
# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if row==1 or row==rows or col==rows//2+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# longest non repeating sub string
# str = "abcbcadbb"
# long = ""
# sub=""

# for i in str:
#     if i not in sub:
#         sub+=i
#     else:
#         if len(sub)>len(long):
#             print(sub)
#             long = sub
#             sub = ""
# print(long)


s = "abcbcadbb"
longest = ""
sub = ""

for i in s:
    if i not in sub:
        sub += i
    else:
        if len(sub) > len(longest):
            longest = sub
        # remove up to and including first occurrence of i
        sub = sub[sub.index(i)+1:] + i

# Final check after loop ends
if len(sub) > len(longest):
    longest = sub

print("Longest non-repeating substring:", longest)
print("Length:", len(longest))

