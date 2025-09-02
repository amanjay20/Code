# def longest_subarray_optimal(arr, K):
#     left = 0
#     right = 0
#     curr_sum = 0
#     max_len = 0

#     while right < len(arr):
#         curr_sum += arr[right]

#         while curr_sum > K:
#             curr_sum -= arr[left]
#             left += 1

#         if curr_sum == K:
#             max_len = max(max_len, right - left + 1)

#         right += 1

#     return max_len
# 🧠 Why it works for only positive numbers (or zero)
# The key idea behind sliding window is:

# You only increase the right pointer to expand the window.

# And if the curr_sum > K, you shrink from the left.

# This logic assumes that:

# Adding more elements always increases or keeps the sum same.

# Removing elements always reduces or keeps the sum same.

# This is true for positive numbers or zero only.