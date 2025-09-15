# ✅ Leaders in an Array
# A leader in an array is an element that is greater than or equal to all the elements to its right.

# 📌 Example:

# Input:  arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# 🧠 Explanation:

# 2 → no elements to right → leader ✅

# 5 > 2 → leader ✅

# 3 < 5 → ❌

# 4 < 5 → ❌

# 17 > all to right → leader ✅

# 16 < 17 → ❌

# 🔎 Approaches
# ✅ 1. Brute Force
# Check for each element if it's greater than all elements to its right.

# python
# Copy
# Edit
# def find_leaders_brute(arr):
#     n = len(arr)
#     leaders = []
#     for i in range(n):
#         is_leader = True
#         for j in range(i+1, n):
#             if arr[j] > arr[i]:
#                 is_leader = False
#                 break
#         if is_leader:
#             leaders.append(arr[i])
#     return leaders
# ⏱ Time: O(n²)

# 🧠 Space: O(1) (excluding output list)

# ✅ 2. Optimal Approach (Right to Left Traversal)
# Start from the end and track the current max.

# python
# Copy
# Edit
# def find_leaders_optimal(arr):
#     n = len(arr)
#     leaders = []
#     max_right = arr[-1]
#     leaders.append(max_right)

#     for i in range(n - 2, -1, -1):
#         if arr[i] >= max_right:
#             leaders.append(arr[i])
#             max_right = arr[i]

#     leaders.reverse()
#     return leaders
# ⏱ Time: O(n)

# 🧠 Space: O(1) (excluding output list)

# ✅ Example Test
# python
# Copy
# Edit
# arr = [16, 17, 4, 3, 5, 2]
# print(find_leaders_optimal(arr))  # Output: [17, 5, 2]