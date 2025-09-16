class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1
        count = 0
        last_smaller = float('-inf')

        if not nums:
            return 0
        
        nums.sort()
        for i in range (n):
            if nums[i]-1 == last_smaller:
                count += 1
                last_smaller = nums[i]
            elif nums[i] != last_smaller:
                count = 1
                last_smaller = nums[i]
            longest = max(longest, count)
        return longest

        