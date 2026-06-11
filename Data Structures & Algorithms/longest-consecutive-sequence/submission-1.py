class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        K = 1
        cntr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] - nums[i - 1] == 1:
                cntr += 1
                K = max(K, cntr)
            else:
                cntr = 1

        return K