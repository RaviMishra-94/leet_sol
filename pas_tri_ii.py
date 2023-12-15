class Solution:
    def generate(self, rowIndex: int) -> list[int]:
        triangle = []

        for num in range(rowIndex + 1):
            row = [1] * (num + 1)
            for j in range(1, num):
                row[j] = triangle[num-1][j-1] + triangle[num-1][j]
            triangle.append(row)
            output = triangle[-1]
        return output


# Create an instance of the class
sol_inst = Solution()

# Call the generate method
rowIndex = 3
pascals_triangle = sol_inst.generate(rowIndex)
print(pascals_triangle)