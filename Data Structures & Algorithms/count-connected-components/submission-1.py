class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Graph = defaultdict(list)
        
        for u,v in edges:
            Graph[u].append(v)
            Graph[v].append(u)
        
        count = [0]
        visited = set()
        def dfs(i):
            visited.add(i)
            for neighbour in Graph[i]:
                if not neighbour in visited:
                    dfs(neighbour)
        res = 0
        for i in range(n):
            if not i in visited:
                dfs(i)
                res += 1
        return res
            

        
        