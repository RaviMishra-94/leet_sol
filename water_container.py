class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))