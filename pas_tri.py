class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for num in range(numRows):
            row = [1] * (num + 1)
            for j in range(1, num):
                row[j] = triangle[num-1][j-1] + triangle[num-1][j]
            triangle.append(row)
        return triangle


# Create an instance of the class
sol_inst = Solution()

# Call the generate method
numRows = 5
pascals_triangle = sol_inst.generate(numRows)
print(pascals_triangle)