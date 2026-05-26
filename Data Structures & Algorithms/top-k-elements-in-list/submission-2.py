class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for num in nums:
            if num not in track:
                track[num] = 0
            track[num] += 1
        track = sorted(track, key=track.get, reverse=True)
        return [v for v in track[:k]]
