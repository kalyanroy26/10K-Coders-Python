# data = {
#     "x":5,
#     "y":2
# }

# for key in data:
#     if key == 'x':
#         print(True)

# data = {'name': 'Ava', 'age': 21}
# print(list(data.keys()))


# data = {
#     "x":5,
#     "y":2
# }
# key = 'z'
# if key not in data:
#     data[key] = 10
# print(data)

# num = 7
# if num%2 == 0:
#     print("even")
# else:
#     print("odd")
        
# num = 5
# def fact(n):
#   if n == 1:
#        return n
#   else:
#        return n*fact(n-1)
# print(fact(num))

# num = 5
# def check_prime(n):
#     fact = 0
#     for i in range(2,n):
#         if n%i == 0:
#             fact+=1
#             break
#     if fact == 0:
#         return "Prime"
#     else:
#         return "Not a Prime"
    
# print(check_prime(num))

# num = 1234
# rev = 0
# while num!=0:
#     digit = num%10
#     rev = rev*10 + digit
#     num = num//10
# print(rev)

num = 12345
count = 0
while num!=0:
    digit = num%10
    count+=1
    num = num//10
print(count)