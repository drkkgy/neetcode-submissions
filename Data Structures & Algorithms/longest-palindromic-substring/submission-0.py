class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd length
            res = self.find_pali(s, i, i, res)
            # even length
            res = self.find_pali(s, i, i+1, res)
        return res

    def find_pali(self, s, l, r, track):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(track):
                track = s[l:r+1]
            l -= 1
            r += 1
        return track