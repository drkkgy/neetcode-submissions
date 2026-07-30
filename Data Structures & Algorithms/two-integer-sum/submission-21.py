class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2:
            return [0,1]

        for index, number in enumerate(nums):
            
            second_num = target - number
            tmp_list = nums.copy()
            tmp_list.pop(index)
            if second_num in tmp_list:
                index2 = nums.index(second_num)
                if index2 < index:
                    return [index2,index]
                elif index2 == index:
                    nums.pop(index)
                    index2 = nums.index(second_num) + 1
                    return [index,index2]
                else:
                    return [index,index2]
