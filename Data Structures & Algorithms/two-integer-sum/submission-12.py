class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for loc,i in enumerate(nums):
            nums[loc] = "X"
            if target-i in nums:
                nums[loc] = "X"
                # # nums.remove(i) 
                # if i == target-i:
                #     nums.remove(i)
                #     return [id1,nums.index(target-i)+1]
                return [loc,nums.index(target-i)]
        