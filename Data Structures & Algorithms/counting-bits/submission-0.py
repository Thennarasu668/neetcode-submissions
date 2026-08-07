class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            for s in bin(i)[2:]:
                if s == "1":
                    count += 1
            res.append(count)
        return res


        