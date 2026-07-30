class Solution:

    def encode(self, strs: List[str]) -> str:
       res=""
       j=0
       for i in strs:
            while j!=len(i):
                res+=f"{ord(i[j])}"+"."
                j+=1
            
            res+=","
            j=0
       return res
    def decode(self, s: str) -> List[str]:
        temp_s=""
        temp=""
        res=[]
        for i in s:
            if i==",":
                res.append(temp_s)
                temp_s=""
            elif i==".":
                temp_s+=chr(int(temp))
                temp=""
            else:
                temp+=f"{i}"
        return res

