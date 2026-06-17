class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minSpeed = right

        while left <= right:
            curr_hours = 0
            mid = left + (right - left) // 2
            for pile in piles:
                curr_hours += math.ceil(pile/mid)
                # while (pile - mid) > 0:
                #     pile -= mid
                #     curr_hours += 1

            if curr_hours > h:
                left = mid + 1
            elif curr_hours <= h:
                minSpeed = min(minSpeed, mid)
                right = mid - 1

        return minSpeed



