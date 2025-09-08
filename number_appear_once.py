# # # .

# # # 🔹 1️⃣ Brute Force Approach (O(n²))

# # # 👉 For every element in the array, count how many times it appears using a nested loop.
# # # If the count is 1 → that’s the single number.

# # # def single_number_bruteforce(nums):
# # #     for i in nums:
# # #         count = 0
# # #         for j in nums:
# # #             if i == j:
# # #                 count += 1
# # #         if count == 1:
# # #             return i


# # # # Example usage
# # # nums = [4, 1, 2, 1, 2]
# # # print("Single Number (Brute):", single_number_bruteforce(nums))


# # # ⏱ Time Complexity → O(n²)
# # # ✅ Works but inefficient for large arrays.

# # 🔹 2️⃣ Better Approach (O(n), O(n) Space – Hash Map)

# # 👉 Count frequency of every number using a dictionary, and return the one with frequency 1.

# # from collections import Counter

# # def single_number_better(nums):
# #     freq = Counter(nums)
    
# #     for num, count in freq.items():
# #         if count == 1:
# #             return num


# # # Example usage
# # nums = [4, 1, 2, 1, 2]
# # print("Single Number (Better):", single_number_better(nums))


# # ⏱ Time Complexity → O(n)
# # 🧱 Space Complexity → O(n) (due to the hash map

# 🔹 3️⃣ Optimal (O(n), O(1) Space – XOR)

# 👉 Simple, efficient solution we discussed before.

# def single_number_optimal(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result


# # Example usage
# nums = [4, 1, 2, 1, 2]
# print("Single Number (Optimal):", single_number_optimal(nums))