#EXCEPTION HANDLING PRACTICE

num = int(input("enter any number: "))

try:
    print(num%0)
except Exception as err:
    print({"error": err})

try:
    print(f"the combination of {num} with hello : {"hello"+num} " )
except Exception as err:
    print({"error":err})

try:
    if num > 0:
        print(f"{num} is a postive number.")
except Exception as err:
    print({"error":err})


#PROBLEM SOLVING 

str1 = "silent"
str2 = "listen"

def check_anagram(str):
    char_count = {}
    for i in str:
        char_count[i] = char_count.get(i,0)+1
    return char_count
    
if  check_anagram(str1) == check_anagram(str2):
    print("The strings are Anagram")
else:
    print("They are not Anagrams")

