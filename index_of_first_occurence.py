class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # If needle is longer than haystack, it can't exist
        if m > n:
            return -1
        
        # Slide window of length m over haystack
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1
