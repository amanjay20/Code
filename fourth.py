# Intersection of Two arrays with Duplicate Elements
# Difficulty: EasyAccuracy: 61.4%Submissions: 32K+Points: 2Average Time: 20m
# Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

# Note: The driver code will sort the resulting array in increasing order before printing.

# Examples:

# Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
# Output: [1, 3]
# Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.
# Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
# Output: [1]
# Explanation: 1 is the only common element present in both the arrays.

#  def intersectionWithDuplicates(self, a, b):
#         freq = {}
#         result = []

#         # Step 1: Store all elements from 'a' in a dictionary
#         for num in a:
#             freq[num] = True  # mark it as present

#         # Step 2: Check elements from 'b'
#         for num in b:
#             if num in freq and freq[num]:  # only add once
#                 result.append(num)
#                 freq[num] = False  # mark as already added

#         return result
