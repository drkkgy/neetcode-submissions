class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        l2 = len(set(nums))

        if l2 < l1:
            return True
        else:
            return False
        