class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for char in s:
            try:
                t.remove(char)
            except:
                return False
        
        if not t:
            return True
        else:
            return False
        