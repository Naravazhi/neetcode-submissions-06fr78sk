class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = float("-inf")


        while left < right:
            curArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(curArea, maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


