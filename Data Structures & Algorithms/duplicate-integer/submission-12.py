class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mem = {}

        for num in nums:
            if num in mem:
                return True
            else:
                mem[num] = 0
        return False
        