class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i <= x:
            i += 1
        return i - 1
    


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid     # mid is a possible answer
                left = mid + 1
            else:
                right = mid - 1
        
        return ans