# 🔹 Optimal Approach (Two Pointers)

# Keep two pointers i and j starting at 0.

# Compare arr1[i] and arr2[j]:

# If equal → add to result and move both pointers.

# If arr1[i] < arr2[j] → move i.

# Else → move j.

# Continue until one array is exhausted.
# def intersection_optimal(arr1, arr2):
#     i, j = 0, 0
#     result = []
    
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] == arr2[j]:
#             if not result or result[-1] != arr1[i]:  # avoid duplicates
#                 result.append(arr1[i])
#             i += 1
#             j += 1
#         elif arr1[i] < arr2[j]:
#             i += 1
#         else:
#             j += 1
    
#     return result


# # Example usage
# arr1 = [1, 2, 4, 5, 6]
# arr2 = [2, 3, 5, 7]

# print("Intersection:", intersection_optimal(arr1, arr2))

# 🔹 Brute Force Idea:

# Loop through every element of the first array.

# For each element, check if it exists in the second array.

# If yes, add it to the result (avoid duplicates if needed).

# Time Complexity → O(n × m) (because of nested loops).
# def intersection_bruteforce(arr1, arr2):
#     result = []
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 if i not in result:   # to avoid duplicates
#                     result.append(i)
#     return result


# # Example usage
# arr1 = [1, 2, 4, 5, 6]
# arr2 = [2, 3, 5, 7]

# print("Intersection:", intersection_bruteforce(arr1, arr2))