class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for s in strs:
           encoded.append(f"{len(s):04d}{s}")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        res=[]
        length=0
        i=0
        while i<len(s):
           current_length=int(s[i:i+4])
           i+=4
           res.append(s[i:i+current_length])
           i+=current_length
           current_length=0
        return res

