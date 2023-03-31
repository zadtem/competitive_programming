class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack= []
        temp=''
      
        for character in s:
            if character != ')':
                stack.append(character)               

            else:
                temp = ''
                while stack[-1] != '(':
                    temp+= stack.pop()
                stack.pop()
                    
                for chr in temp:
                    stack.append(chr)

        reverse = ''.join(stack)
        return reverse
