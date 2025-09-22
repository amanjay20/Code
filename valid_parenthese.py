class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # it's a closing bracket
                top = stack.pop() if stack else '#'  # handle empty stack safely
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)  # opening bracket
        
        return not stack  # valid only if stack is empty