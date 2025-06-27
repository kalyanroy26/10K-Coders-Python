# def are_heights_equal(h1,h2,v1,v2):

#     #if velocities are equal and heights are not equal they never meet
#     if v1==v2:
#         return h1==h2
    
#     if (v1==0 and h1!=h2) or (v2==0 and h1!=h2):
#         return False
    
#     while True:
#         #if heights are equal return True
#         if h1 == h2:
#             return True
        
#         # If one surpasses the other and velocities do not catch up (One Overtakes the Other)
#         if (h1>h2 and v1>=v2) or (h2>h1 and v2>=v1):
#             return False
        
#         h1+=v1
#         h2+=v2


# print(are_heights_equal(2, 4, 0, 2))  # ➡️ False (h1 is stuck, h2 keeps moving)
# print(are_heights_equal(2, 4, 2, 2))  # ➡️ True (both move equally)
# print(are_heights_equal(5, 8, 1, 3))  # ➡️ False (h2 keeps getting further away)
# print(are_heights_equal(3, 6, 1, 1))  # ➡️ False (same speed, different height)
# print(are_heights_equal(5, 5, 0, 0))  # ➡️ True (both are the same, no movement)
# print(are_heights_equal(5, 8, 0, 0))  # ➡️ False (both are stuck and not equal)



def combinations(iterable):

    if sum(iterable)==6:
        print(iterable)
        
    if len(iterable) == 0:
        return [[]]
    
    combos = []

    for combo in combinations(iterable[1:]):
        combos += [combo + [iterable[0]], combo]
    
    return combos


numbers = [1,2,3,4]

combos = combinations(numbers)

