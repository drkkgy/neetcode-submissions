class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track_dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in track_dict:
                track_dict[key] = []
            track_dict[key].append(word)
        return list(track_dict.values())
        