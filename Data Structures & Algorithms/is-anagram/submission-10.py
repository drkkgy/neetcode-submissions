class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_lis = list(t)
        del t
        for char in s:
            if char in t_lis:
                t_lis.remove(char)
            else:
                return False
        if not t_lis:
            return True
        return False