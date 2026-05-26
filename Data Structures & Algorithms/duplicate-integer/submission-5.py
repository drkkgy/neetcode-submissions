class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		buffer = []
		for i in nums:
			if i in buffer:
				return True
			buffer.append(i)
		return False


        