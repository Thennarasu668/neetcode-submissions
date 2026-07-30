class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        for r,c in queue:
            for row,col in directions:
                ro = r + row
                co = c + col
                if 0 <= ro < len(grid) and 0 <= co < len(grid[0]) and grid[ro][co] == 2147483647:
                    grid[ro][co] = grid[r][c] + 1
                    queue.append((ro,co))
            