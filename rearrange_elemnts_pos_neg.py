class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
       
        pos = 0 
        neg = 1
        n = len(nums)
        ans = [0] * n
        for i in range (n):
            if nums[i] > 0 :
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans
