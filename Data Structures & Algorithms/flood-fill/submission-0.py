class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        st_color = [image[sr][sc]]
        def dfs(i,j,color):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == st_color[0]:
                image[i][j] = color
                dfs(i,j + 1,color)
                dfs(i,j - 1,color)
                dfs(i + 1,j,color)
                dfs(i - 1,j,color)
            
        dfs(sr,sc,color)
        return image
        