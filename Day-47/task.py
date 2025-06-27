# # def generate_subsets(nums):
# #     nums.sort()
# #     results = []

# #     def backtrack(start, current):
# #         results.append(current[:])
        
# #         for i in range(start,len(nums)):
# #             if i>start and nums[i] == nums[i-1]:
# #                 continue
# #             current.append(nums[i])
# #             backtrack(i+1, current)
# #             current.pop()

# #     backtrack(0, [])

# #     return results

# # # print(generate_subsets([1,2,2]))



# # # possible set of combinations sum is equal to target
# # def combination_sum(nums, target):
# #     results = []
# #     def backtrack(start, current, current_sum):
# #         if current_sum == target:
# #             results.append(current[:])
# #             return
        
# #         if current_sum > target:
# #             return
        
# #         for i in range(start, len(nums)):
# #             current.append(nums[i])
# #             backtrack(i+1, current, current_sum+nums[i])
# #             current.pop()

    
# #     backtrack(0,[],0)

# #     return results

# # print(combination_sum([1,2], 3))


# def generateSubset(nums):
#     nums.sort()
#     result = []

#     def backtrack(start,current):
#         result.append(current[:])

#         for i in range(start, len(nums)):
#             if i>start and nums[i]==nums[i-1]:
#                 continue
#             current.append(nums[i])
#             backtrack(i+1, current)
#             current.pop()
        
#     backtrack(0,[])

#     return result

# print(generateSubset([1,2,3,4]))


def combinationSum(nums, target):
    result = []

    def backtrack(start, current, current_sum): #helper function 
        if current_sum == target:       #if current_sum is equal to target then only append and return 
            result.append(current[:])
            return
        
        if current_sum > target: #if current_sum is greater than target then return 
            return
        
        for i in range(start, len(nums)):
            current.append(nums[i])         #append and element from nums list
            backtrack(i+1,current, current_sum+nums[i])     #check whether the element can give target but using recursive backtrack
            current.pop()       #remove last appended element 
    
    backtrack(0,[],0)  # initial start

    return result

print(combinationSum([1,2,3,4,6,3],6))


