class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                t = t.replace(char,"+",1)
            else:
                return False
        if len(set(t)) == 1: 
            return True
        else:
            return False
                
        