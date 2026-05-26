class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]

                    if triplet not in triplets:
                        triplets.append(triplet)

                    left += 1
                    right -= 1

                elif total_sum < 0:
                    left += 1

                else:
                    right -= 1

        return triplets
 




        