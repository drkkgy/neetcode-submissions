class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # if not tails:
            #     tails.append(num)
            # elif tails[-1] >= num:
            #     tails[-1] = num
            # else:
            #     tails.append(num)

            left,right = 0,len(tails)

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid


            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)



        