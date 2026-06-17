class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        r,l = len(numbers)-1,0

        while l < r:
            # if numbers[r] >= target:
            #     r -= 1
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []


        