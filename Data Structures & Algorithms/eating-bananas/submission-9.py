class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # piles = [3, 4, 2, 4, 5] each pile has x amt of bananas
        # we have h hours to eat them

        # we need to figure out how 
        

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > h:
                left = mid + 1
            elif time <= h:
                #right = mid - 1 # dont do mid - 1 becaise if it works we dont want to throw away when we return
                right = mid
        # return mid
        return left
        # left is smallest k we haven't ruled out
        # right is the largest k we haven't ruled out
