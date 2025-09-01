# Find the union in two sorted array
# class Solution:
#     # Function to return a list containing the union of the two arrays.
#     def findUnion(self, a, b):
#         n1 = len(a)
#         n2 = len(b)
#         i = 0
#         j = 0
#         unionArr = []
        
#         # Merge the two arrays
#         while (i < n1) and (j < n2):
#             # Avoid duplicates
#             if a[i] == b[j]:
#                 if not unionArr or unionArr[-1] != a[i]:
#                     unionArr.append(a[i])
#                 i += 1
#                 j += 1
#             elif a[i] < b[j]:
#                 if not unionArr or unionArr[-1] != a[i]:
#                     unionArr.append(a[i])
#                 i += 1
#             else:
#                 if not unionArr or unionArr[-1] != b[j]:
#                     unionArr.append(b[j])
#                 j += 1
        
#         # Add remaining elements from a
#         while i < n1:
#             if not unionArr or unionArr[-1] != a[i]:
#                 unionArr.append(a[i])
#             i += 1
        
#         # Add remaining elements from b
#         while j < n2:
#             if not unionArr or unionArr[-1] != b[j]:
#                 unionArr.append(b[j])
#             j += 1
        
#         return unionArr

# # Test cases
# sol = Solution()
# print(sol.findUnion([1, 2, 3, 4, 5], [1, 2, 3, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
# print(sol.findUnion([2, 2, 3, 4, 5], [1, 1, 2, 3, 4]))  # [1, 2, 3, 4, 5]
# print(sol.findUnion([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]))  # [1, 2]
