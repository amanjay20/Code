# IF MATRIX IS SORTED 
# class Solution:
#     def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
#         n = len(mat)
#         m = len(mat[0])

#         # Helper function to find first index of 1 in a sorted row
#         def lowerBound(arr, n, x):
#             low = 0
#             high = n - 1
#             ans = n
#             while low <= high:
#                 mid = (low + high) // 2
#                 if arr[mid] >= x:
#                     ans = mid
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             return ans

#         index = 0
#         cnt_max = 0

#         for i in range(n):
#             # find first occurrence of 1 in row i
#             lb = lowerBound(mat[i], m, 1)
#             count_ones = m - lb  # total 1s = total elements - index of first 1

#             if count_ones > cnt_max:
#                 cnt_max = count_ones
#                 index = i

#         return [index, cnt_max]

# ///// IF NOT SORTED 
# class Solution:
#     def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
#         max_ones = -1
#         index = 0

#         for i, row in enumerate(mat):
#             count = sum(row)            # safe even if row is unsorted
#             if count > max_ones:       # strictly greater keeps smallest index on ties
#                 max_ones = count
#                 index = i

#         return [index, max_ones]
