class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in tracker:
                tracker[sorted_word] = []
            
            tracker[sorted_word].append(word)
        return list(tracker.values())
                
                
        
        