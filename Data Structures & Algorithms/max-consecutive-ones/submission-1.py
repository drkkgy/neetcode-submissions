class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0

        track = 0
        counter = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                counter += 1
            else:
                track = max(track,counter)
                counter = 0
        track = max(track,counter)
        return track


        