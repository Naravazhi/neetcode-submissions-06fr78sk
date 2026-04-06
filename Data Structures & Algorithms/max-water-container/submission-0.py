class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = float("-inf")

        while left < right:
            length = right - left
            limiting_height = min(heights[left], heights[right])
            curArea = length * limiting_height
            maxArea = max(maxArea, curArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        if maxArea == float("-inf"):
            return 0
        else:
            return maxArea
        #return 0 if maxArea = float("-inf") else maxArea
