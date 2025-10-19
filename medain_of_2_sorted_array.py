# BRUTE FORCE 
# Class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums3 = [] // we take an extra array here 
#         n1 = len(nums1)
#         n2 = len(nums2)
#         i = 0
#         j = 0
#         while ((i<n1) and (j<n2)):
#             if nums1[i] < nums2[j]:
#                 nums3.append(nums1[i])
#                 i+=1
#             else:
#                 nums3.append(nums2[j])
#                 j+=1
#         while (i<n1):
#             nums3.append(nums1[i])
#             i+=1
#         while (j<n2):
#             nums3.append(nums2[j])
#             j+=1

#         n = n1+n2
#         if (n%2==1):
#             return nums3[n//2]
#         return (nums3[n//2] + nums3[(n//2)-1])/2

# ////////////////////////////////////////////////

# // Here we have removed the extra space that we take in brute force approach 
# // Here we used Two pointer not to store element we used it to get medain 
# class Solution:
# def findMedianSortedArrays(self, nums1, nums2):
#         n1, n2 = len(nums1), len(nums2)
#         n = n1 + n2

#         i = j = 0
#         count = 0
#         m1 = m2 = 0

#         median_pos1 = (n - 1) // 2
#         median_pos2 = n // 2

#         while i < n1 or j < n2:
#             if j >= n2 or (i < n1 and nums1[i] < nums2[j]):
#                 val = nums1[i]
#                 i += 1
#             else:
#                 val = nums2[j]
#                 j += 1

#             if count == median_pos1:
#                 m1 = val
#             if count == median_pos2:
#                 m2 = val
#                 break
#             count += 1

#         return (m1 + m2) / 2.0


