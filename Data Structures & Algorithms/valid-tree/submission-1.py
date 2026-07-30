from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(i):
            visited.add(i)
            for neighbor in adj[i]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n