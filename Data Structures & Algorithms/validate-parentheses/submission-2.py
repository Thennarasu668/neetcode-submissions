class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mymap = {']':'[','}':'{',')':'('}
        for b in s:
            if b in mymap:
                if not stack or mymap[b] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        return len(stack) == 0
        