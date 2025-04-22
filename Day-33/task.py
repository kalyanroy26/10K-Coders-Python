# 1) Print the multiple of 5 in a list using map and filter
list1 = [2,10,15,19,20,2,5,30,25,45]

out = map(lambda x: x%5==0, list1)
out = list(out)
print(out)


#2)Print the vowels in the string using map and filter
vowels = "aeiouAEIOU"
string = "confidence buids overconfidence kills"

out2 = filter(lambda char : char in vowels ,string)
out2 = list(out2)
print(out2)