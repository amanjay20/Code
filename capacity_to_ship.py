class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysReq(capacity):
            day , load = 1, 0
            for item in weights:
                if (load+item) > capacity:
                    day += 1
                    load = item
                    if day > days:
                        return False
                else:
                    load += item
            return day <= days
        low = max(weights)
        high = sum(weights)
        while (low<=high):
            mid = (low+high)//2
            if daysReq(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans 

        