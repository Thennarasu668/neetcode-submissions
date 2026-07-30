class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        left = 0
        res = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == "W":
                count += 1
            if r - left + 1 == k:
                res = min(res, count)
                if blocks[left] == "W":
                    count -= 1
                left += 1
                
            
        return res

