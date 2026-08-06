class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            s = ord('A') + rem 
            res += chr(s)
            columnNumber //= 26
            
        return res[::-1]
