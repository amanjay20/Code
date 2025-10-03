def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k:int)-> bool:
            hours = 0
            for P in piles:
                hours += (P+k-1)//k
                if hours > h:
                    return False
            return hours <= h
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low+high) // 2
            if can_finish(mid):
                ans = mid
                high = mid -1
            else:
                low = mid +1 
        return ans