class Solution:
    def maxDifference(self, s: str) -> int:
        if not s:
            return 0
        freq_map = {}
        for l in s:
            freq_map[l] = freq_map.get(l,0) + 1
        
        even_min = float('inf')
        odd_max = float('-inf')
        for k,v in freq_map.items():
            if v % 2:
                odd_max = max(odd_max,v)
            else:
                even_min = min(even_min,v)
        return odd_max - even_min
            
        