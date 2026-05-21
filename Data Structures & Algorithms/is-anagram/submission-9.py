class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for a in list(s):
            if a in t:
                t.remove(a)
            else:
                return False
        if not t:
            return True
        return False
        