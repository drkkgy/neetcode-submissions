class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','',s)

        pt1,pt2 = 0,len(s)-1

        while pt1 <= pt2:

            if s[pt1] != s[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        return True
        