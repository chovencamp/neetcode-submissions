class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # If the new color is the same as the original, no need to fill
        if original_color == color:
            return image
            
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check boundaries and whether the current pixel matches the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Update the pixel to the new color
            image[r][c] = color
            
            # Recursively fill in all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image