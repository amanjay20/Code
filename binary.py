#  def search(self, nums: List[int], target: int) -> int:
#         low = 0 
#         high = len(nums) - 1
#         while low <= high:
#             mid = int((low + high) / 2)
#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 low = mid+1
#             else:
#                 high = mid -1
#         return -1
# ///Iterative code of Binary search 

# ///Recusrsive Code 
# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return self.binary_search(nums, target, 0, len(nums) - 1)

#     def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        
#         if left > right:
#             return -1

#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             # Search in the right half
#             return self.binary_search(nums, target, mid + 1, right)
#         else:
#             # Search in the left half
#             return self.binary_search(nums, target, left, mid - 1)
