class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m* k > n:
            return -1
        def possible(bloomDay,day,m,k):
            count = 0
            bouqets = 0
            for i in range (n):
                if bloomDay[i]<= day:
                    count += 1
                    if count == k:
                        bouqets += 1
                        count = 0
                else:
                    count = 0
            
            return bouqets >= m

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if possible(bloomDay,mid,m,k):
                ans = mid
                high = mid -1
            else:
                low = mid +1
            
        return ans 