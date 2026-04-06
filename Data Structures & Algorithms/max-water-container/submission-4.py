class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")
        
        left = 0
        right = len(heights) - 1

        while left < right:
            smaller = min(heights[left], heights[right])
            area = (right - left) * smaller
            maxArea = max(area, maxArea)
            if smaller == heights[left]:
                left += 1
            else:
                right -= 1

        return maxArea