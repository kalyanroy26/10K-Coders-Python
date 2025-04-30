# #p1
# p = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(p)):
#     if p[i]%2 == 0:
#         p[i] = p[i]*2
#     else:
#         p[i] = p[i]

# print(p)

# #p2
# for i in range(10,20):
#     if i%2==0:
#         print(i)

# print('\n')

# #p3
# for i in range(10,20):
#     if i%2!=0:
#         print(i)

# p4
# p = [1,2,3,4,5,6,7,8,"python",True]

# for i in range(len(p)):
#     if type(p[i]) == int and p[i]%2!=0:
#        p[i] = p[i]*2
#     else:
#         p[i] = p[i]

# print(p)

#p5 
# p = [1,10,20,30,50,60]
# sum = 0
# for i in p:
#     sum+=i
# print(sum)

#p6

# string = "Python"
# rev = ''
# for i in range(len(string)-1,-1,-1):
#     rev+=string[i]
# print(rev)

#p7
# list = [2,4,2,3,2,4,6,4,5,5,7,8,9]
# list1 = []

# for ele in list:
#     if ele not in list1:
#         list1.append(ele)

# print(list1)

# #p8
# list1 = [2, 4, 3, 6, 5, 7, 8, 9]
# count=0

# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[j]>list1[i]:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print(list1,count)

#
# list1 = [2, 4, 3, 6, 5, 7, 8, 9]
# max = list1[0]
# min = list1[0]
# for i in list1:
#     if i > max:
#         max = i
    
#     if i < min:
#         min = i
# print(max, min)

#p8
# string = "python DEveloper"
# new_str = ""

# for i in string:
#     if 97<=ord(i)<=122:
#         asc = ord(i)-32
#         new_asc = chr(asc)
#         new_str+=new_asc
#     elif 65<=ord(i)<=91:
#         asc = ord(i)+32
#         new_asc = chr(asc)
#         new_str+=new_asc

# print(new_str)

#p9
# s = ['aaa','a','aa','aaaa']

# for i in range(len(s)):
#     for j in range(len(s)):
#         if len(s[i])<len(s[j]):
#             temp = s[i]
#             s[i] = s[j]
#             s[j] = temp

# print(s)

#p10
num = 28
sum = 0
for i in range(1,num):
    if num%i==0:
        sum+=i

if num == sum:
    print("perfect")



