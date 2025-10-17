# 🧠 Your Brute Force Idea

# You’re trying to:

# Track how many new stations are added between each pair of existing stations (howmany list).

# Each time, add a new station to the segment that currently has the largest distance between stations.

# Repeat until you’ve added all k stations.

# Finally, return the maximum distance among all segments.

# ✅ This logic is correct conceptually — this is the greedy approach (though inefficient).
# But there are some implementation issues that break the code.




# class Solution:
#     def minMaxDist(self, stations, k):
#         n = len(stations)
#         if n <= 1:
#             return 0.00
#         howmany = [0] * (n-1)
#         for gasStation in range (k):
#             maxSection = -1
#             maxInd = -1
#             for i in range (n-1):
#                 diff = stations[i+1] - stations[i]
#                 sectionLength = diff / (howmany[i]+1)
#                 if sectionLength > maxSection:
#                     maxSection = sectionLength
#                     maxInd = i
#             if maxInd != -1:
#                 howmany[maxInd] += 1
#         maxAns = 0
#         for i in range (n-1):
#             diff = stations[i+1] - stations[i]
#             sectionLength = diff / (howmany[i]+1)
#             maxAns = max(maxAns,sectionLength)
#         return round(maxAns,2)