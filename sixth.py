# def longest_subarray_better(arr, K):
#     prefix_sum_map = {}
#     curr_sum = 0
#     max_len = 0

#     for i in range(len(arr)):
#         curr_sum += arr[i]

#         if curr_sum == K:
#             max_len = i + 1

#         if (curr_sum - K) in prefix_sum_map:
#             length = i - prefix_sum_map[curr_sum - K]
#             max_len = max(max_len, length)

#         if curr_sum not in prefix_sum_map:
#             prefix_sum_map[curr_sum] = i

#     return max_len
# 🧠 Core Logic:
# Maintain a running sum (curr_sum).

# For each index i, check if there was a prefix sum such that removing it gives sum K.
# → That is: if curr_sum - K is in the hashmap, then a subarray from that index + 1 to i has sum = K.

# Loop begins:
# 🔹 i = 0 → arr[0] = 1
# python
# Copy
# Edit
# curr_sum = 0 + 1 = 1

# 1 != K → skip

# (1 - 3 = -2) not in map → skip

# 1 not in map → add: {1: 0}
# 🔹 i = 1 → arr[1] = 2
# python
# Copy
# Edit
# curr_sum = 1 + 2 = 3

# curr_sum == K → max_len = i+1 = 2 ✅

# (3 - 3 = 0) not in map → skip

# 3 not in map → add: {1:0, 3:1}
# 🔹 i = 2 → arr[2] = 3
# python
# Copy
# Edit
# curr_sum = 3 + 3 = 6

# 6 != K → skip

# (6 - 3 = 3) in map at index 1
# → length = i - map[3] = 2 - 1 = 1
# → max_len = max(2, 1) = 2

# 6 not in map → add: {1:0, 3:1, 6:2}
# 🔹 i = 3 → arr[3] = 1
# python
# Copy
# Edit
# curr_sum = 6 + 1 = 7

# (7 - 3 = 4) not in map → skip

# 7 not in map → add: {1:0, 3:1, 6:2, 7:3}
# 🔹 i = 4 → arr[4] = 1
# python
# Copy
# Edit
# curr_sum = 7 + 1 = 8

# (8 - 3 = 5) not in map → skip

# 8 not in map → add: {1:0, 3:1, 6:2, 7:3, 8:4}
# 🔹 i = 5 → arr[5] = 1
# python
# Copy
# Edit
# curr_sum = 8 + 1 = 9

# (9 - 3 = 6) in map at index 2
# → length = 5 - 2 = 3 ✅
# → max_len = max(2, 3) = 3

# 9 not in map → add: {1:0, 3:1, 6:2, 7:3, 8:4, 9:5}
# 🔹 i = 6 → arr[6] = 1
# python
# Copy
# Edit
# curr_sum = 9 + 1 = 10

# (10 - 3 = 7) in map at index 3
# → length = 6 - 3 = 3
# → max_len = max(3, 3) = 3

# 10 not in map → add
# ✅ Final Result:
# python
# Copy
# Edit
# return max_len = 3