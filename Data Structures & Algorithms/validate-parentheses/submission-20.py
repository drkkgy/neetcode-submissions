class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:

            if not stack:
                stack.append(char)
            else:
            
                if char == ')' and stack[-1] == '(':
                    stack.pop(-1)
                
                elif char == '}' and stack[-1] == '{':
                    stack.pop(-1)

                elif char == ']' and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    stack.append(char)

        if not stack:
            return True
        else:
            return False


            

            
        