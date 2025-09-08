# .

# 🔹 1️⃣ Brute Force Approach (O(n²))

# 👉 For every element in the array, count how many times it appears using a nested loop.
# If the count is 1 → that’s the single number.

# def single_number_bruteforce(nums):
#     for i in nums:
#         count = 0
#         for j in nums:
#             if i == j:
#                 count += 1
#         if count == 1:
#             return i


# # Example usage
# nums = [4, 1, 2, 1, 2]
# print("Single Number (Brute):", single_number_bruteforce(nums))


# ⏱ Time Complexity → O(n²)
# ✅ Works but inefficient for large arrays.