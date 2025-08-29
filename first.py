# 26. Remove Duplicates from Sorted Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         i = 0
#         for j in range (1,n):
#             if nums[j] != nums[i]:
#                 nums[i+1] = nums[j]
#                 i+=1
#         return i+1
