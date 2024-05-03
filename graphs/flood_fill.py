"""
733. Flood Fill
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
"""
from typing import List
from collections import deque

def bfs(image, sr, sc, color):
    row_len = len(image)
    col_len = len(image[0])
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = deque()
    queue.append((sr, sc))
    oldColor = image[sr][sc]
    image[sr][sc] = color
    while queue:
        current_row, current_col = queue.popleft()
        for delta_row, delta_col in directions:
            new_row = current_row + delta_row
            new_col = current_col + delta_col
            if (0 <= new_row < row_len) and (0 <= new_col < col_len) \
                and (image[new_row][new_col] == oldColor):
                    queue.append((new_row, new_col))
                    image[new_row][new_col] = color
            
    
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    bfs(image, sr, sc, color)
    return image


print(flood_fill([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
], 0, 2, 5))
        
    
    