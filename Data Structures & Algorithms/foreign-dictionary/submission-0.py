from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        unique  = set()
        for w in words:
            for l in w:
                unique.add(l)
        visit = {}
        for i in range(1,len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            min_len = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if not w2[j] in w1[j]:
                        graph[w1[j]].add(w2[j])
                    break
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in graph[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for l in unique:
            if dfs(l):
                return ""
        return "".join(res)[::-1]
            


        
                    


            



        