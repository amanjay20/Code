# class Solution:
# 	def longestSubarrayDivK(self, arr, k):
# 		#Complete the function
# # 		max_len = 0 
# # 		n = len(arr)
# # 		for i in range (n):
# # 		    sum = 0 
# # 		    for j in range (i, n):
# # 		        sum += arr[j]
# # 		        if sum % k == 0:
# # 		            max_len = max(max_len , j-i+1)
# #         return max_len
#         prefix_sum = 0 
#         prefix_map = {}
#         max_len = 0
#         n = len(arr)
#         for i in  range (n):
#             prefix_sum += arr[i]
#             mod = prefix_sum % k
            
#             if mod < 0:
#                 mod +=k
                
#             if mod ==0:
#                 max_len = i+1
            
#             if mod in prefix_map:
#                 max_len = max(max_len, i - prefix_map[mod])
#             else:
#                 prefix_map[mod] = i
                
#         return max_len