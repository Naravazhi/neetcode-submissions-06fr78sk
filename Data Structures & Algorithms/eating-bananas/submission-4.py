class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) # cause you cant go to another pile

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            ptr = 0
            while ptr < len(piles):
                hours += math.ceil(piles[ptr] / mid)
                ptr += 1
                # currVal = piles[ptr]
                # while currVal - mid > 0:
                #     currVal -= mid
                #     hours += 1
                # else: # pile - mid <= 0
                #     hours += 1
                #     ptr += 1
                #     continue

            if hours > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans


























