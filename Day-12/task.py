# num = 55
# no_of_primes = 0
# while True:
#     num+=1
#     count = 0
#     for i in range (1,num+1):
#         if num%i == 0:
#             count+=1
#     if count == 2:
#         no_of_primes+=1
#     if no_of_primes == 2:
#         print("second prime is ",num)
#         break
        



my_details = {
    "name": "kalyan maharajulu",
    "age": 23,
    "education": "Bachelors in CSE",
    "skills": ['HTML','CSS','javascript','react.js','node.js','Git', 'postman'],
    "batch": "37R"
}

print(my_details.get("name"),'\n')

print(my_details.keys())

print(my_details.values(),'\n')

print(my_details.items(),'\n')

print(len(my_details['skills']),'\n')