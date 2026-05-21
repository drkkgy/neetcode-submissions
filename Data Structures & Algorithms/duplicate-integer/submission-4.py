class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        buff = []
        for i in nums:
            if i in buff:
                return True
            buff.append(i)
        return False

        