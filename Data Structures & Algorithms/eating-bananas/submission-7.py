class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minimum_k = max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            i = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)

                # while pile > 0:
                #     pile -= mid
                #     hours += 1
            
            # what should be condition? cause h = 8 is > h = 7 when we have the 3, 6, 7, 11

            if hours > h:
                left = mid + 1

            elif hours <= h:
                minimum_k = mid
                right = mid - 1

        return minimum_k
                




















# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left = 1
#         right = max(piles) # cause you cant go to another pile

#         while left <= right:
#             mid = left + (right - left) // 2
#             hours = 0
#             ptr = 0
#             while ptr < len(piles):
#                 hours += math.ceil(piles[ptr] / mid)
#                 ptr += 1
#                 # currVal = piles[ptr]
#                 # while currVal - mid > 0:
#                 #     currVal -= mid
#                 #     hours += 1
#                 # else: # pile - mid <= 0
#                 #     hours += 1
#                 #     ptr += 1
#                 #     continue

#             if hours > h:
#                 left = mid + 1
#             else:
#                 ans = mid
#                 right = mid - 1
#         return ans




























