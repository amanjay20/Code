# 1️⃣ Brute Force Approach
# Idea: Check every possible pair.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# 2️⃣ Better Approach using Hash Map
# Idea: Store each element's index in a map. For each element x, check if target - x exists.

# Time Complexity: O(n)
# Space Complexity: O(n)

# def twoSum(nums, target):
#     index_map = {}  # value -> index
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in index_map:
#             return [index_map[diff], i]
#         index_map[num] = i

# 3️⃣ Optimal for Sorted Arrays (Two Pointers)
# ⚠️ Only works if the array is sorted and you're asked to return the values, not indices.

# Time Complexity: O(n)

# Space Complexity: O(1)


# def twoSumSorted(nums, target):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         curr_sum = nums[left] + nums[right]
#         if curr_sum == target:
#             return [left, right]
#         elif curr_sum < target:
#             left += 1
#         else:
#             right -= 1
# 🎯 Recommended for Interviews: Better (Hash Map) Approach
# It’s optimal in both time and practical use cases.
# Let me know if you want this in JavaScript or want to see dry runs for better understanding.