from typing import List

"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution():
    def rotateImage(self, image: List[List[int]]) -> List[List[int]]:
        rotated_image = [[0]*len(image[0]) for _ in range(len(image))]
        cnt = len(image) - 1
        for i in range(len(image)):
            for j in range(len(image[0])):
                rotated_image[j][cnt] = image[i][j]
            cnt -= 1
        print(rotated_image)
        
    def rotateImageSpaceOptimal(self, image: List[List[int]]) -> List[List[int]]: 
        n = len(image)
        # Transpose the image
        for i in range(n):
            for j in range(i, n):
                image[i][j], image[j][i] = image[j][i], image[i][j]
        # Reverse each of the rows
        for i in range(n):
            for j in range(n // 2):
                image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]
        return image

s = Solution()
print(s.rotateImageSpaceOptimal([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))