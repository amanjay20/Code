class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # start from last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:       # if not 9, just add 1 and return
                digits[i] += 1
                return digits
            digits[i] = 0           # if 9, make it 0 and carry goes left
        
        # if all were 9 → new array like [1,0,0,0...]
        return [1] + digits