# 🔹 1️⃣ Brute Force Approach (O(n²))

# 👉 For every element, count how many times it appears using a nested loop.

# def majority_element_bruteforce(nums):
#     n = len(nums)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if nums[j] == nums[i]:
#                 count += 1
#         if count > n // 2:
#             return nums[i]


# # Example usage
# nums = [3, 3, 4, 2, 3, 3, 3]
# print("Majority Element (Brute):", majority_element_bruteforce(nums))


# ⏱ Time Complexity → O(n²)
# 🧱 Space Complexity → O(1)
# //////////////////////////////////////////////////////

# 🔹 2️⃣ Better Approach (O(n), O(n) Space – Hash Map)

# 👉 Count frequencies using a dictionary and find the element with frequency > n // 2.

# from collections import Counter

# def majority_element_better(nums):
#     n = len(nums)
#     freq = Counter(nums)
    
#     for num, count in freq.items():
#         if count > n // 2:
#             return num


# # Example usage
# nums = [3, 3, 4, 2, 3, 3, 3]
# print("Majority Element (Better):", majority_element_better(nums))


# ⏱ Time Complexity → O(n)
# 🧱 Space Complexity → O(n)