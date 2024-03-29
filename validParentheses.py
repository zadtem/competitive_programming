class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesPairs = {")" : "(", "]" : "[", "}" : "{"} 
        stack = []
        for c in s:
            if c in parenthesesPairs:
                if stack and stack[-1] == parenthesesPairs[c]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)
      if not stack:
            return True
        else:
            return False