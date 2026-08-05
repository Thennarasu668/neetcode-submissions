class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map1 = {}
        freq_map2 = {}
        for s in ransomNote:
            freq_map1[s] = freq_map1.get(s,0) + 1
        for s in magazine:
            freq_map2[s] = freq_map2.get(s,0) + 1
        for k,v in freq_map1.items():
            if k not in freq_map2:
                return False
            if freq_map2[k] < v:
                return False
        return True
            
            