class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = []
        for i in range(len(nums)):
            prod = -30
            for j in range(len(nums)):
                # if i == j:
                #     pass
                if prod == -30 and i !=j:
                    prod = nums[j]
                elif i == j:
                    prod = prod
                else:
                    prod = prod*nums[j]
            outputs.append(prod)
        return outputs

        