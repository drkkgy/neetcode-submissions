class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        
        K = 1
        
        count  = 1

        for i in range(1,len(nums)):

            if nums[i-1] == nums[i]:
                continue
            
            elif nums[i] - nums[i-1] == 1:
                count += 1
                K = max(K,count)

            else:
                count = 1

        return K 


            





        
        