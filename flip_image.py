class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        image = [imag[::-1] for imag in image]
        print(image)
    
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else: image[i][j] = 0
        return image
     




image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))
        