class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = {}
        for c in arr:
            freq_map[c] = freq_map.get(c,0) + 1
        
        c = 0
        for key,v in freq_map.items():
            if v == 1:
                c += 1
                if c == k:
                    return key
        return ""