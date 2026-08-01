class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for l in s:
            freq_map[l] = freq_map.get(l,0) + 1
        even = 0
        odd = 0
        print(freq_map)
        for k,v in freq_map.items():
            if v % 2 == 1:
                if odd < v:
                    if odd > 0:
                        even += (odd - 1)
                    odd = v
                else:
                    even += (v - 1)
            else:
                even += v
        return even + odd
 
            
         