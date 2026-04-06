class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True



        while l <= r:
            cap = r + (l - r) // 2
            if canShip(cap):
                res = min(cap, res)
                r = cap - 1
            else:
                l = cap + 1
        return res



        # res = max(weights)

        # while True:
        #     ships = 1
        #     cap = res
        #     for w in weights:
        #         if cap - w < 0: 
        #             ships += 1
        #             cap = res
        #         cap -= w
        #     if ships <= days:
        #         return res

        #     res += 1


        # weights

        # days