# # class Solution:
# #     def longestConsecutive(self, nums: List[int]) -> int:
# #         n = len(nums)
# #         longest = 1
# #         count = 0
# #         last_smaller = float('-inf')

# #         if not nums:
# #             return 0
        
# #         nums.sort()
# #         for i in range (n):
# #             if nums[i]-1 == last_smaller:
# #                 count += 1
# #                 last_smaller = nums[i]
# #             elif nums[i] != last_smaller:
# #                 count = 1
# #                 last_smaller = nums[i]
# #             longest = max(longest, count)
# #         return longest

#         class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # count = 0
#         # last_smaller = float('-inf')

#         # if not nums:
#         #     return 0
        
#         # nums.sort()
#         # for i in range (n):
#         #     if nums[i]-1 == last_smaller:
#         #         count += 1
#         #         last_smaller = nums[i]
#         #     elif nums[i] != last_smaller:
#         #         count = 1
#         #         last_smaller = nums[i]
#         #     longest = max(longest, count)
#         # return longest
#         if not nums :
#             return 0
#         num_sets = set(nums)
#         longest = 0

#         for num in num_sets:
#             if num-1 not in num_sets:
#                 current_num = num
#                 current_streak = 1

#                 while current_num + 1 in num_sets:
#                     current_num += 1
#                     current_streak += 1
#                 longest = max(longest,current_streak)
#         return longest


        