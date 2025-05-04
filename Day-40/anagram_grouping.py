list1 = ['ate','eat','tea','bat','tab','tan','nat']

keys = []
anagram_dic = {}

for ele in list1:  #loop to find sorted key from list1
    temp = ''.join(sorted(ele))
    if temp not in keys:
        keys.append(temp)

for key in keys:    #loop to create empty list value using keys from keys list
    anagram_dic[key] = []

for ele in list1:   #loop to find and add element from list1 to anagram dictionary 
    temp = ''.join(sorted(ele))
    if temp in keys:
        anagram_dic[temp].append(ele)
    
print(anagram_dic)
    
#program 2 using collections
from collections import defaultdict

list1 = ['ate','eat','tea','bat','tab','tan','nat']
anagram_dic = defaultdict(list)

for ele in list1:  
    key = ''.join(sorted(ele))
    anagram_dic[key].append(ele)

anagram_dic = dict(anagram_dic)

print(anagram_dic)
    