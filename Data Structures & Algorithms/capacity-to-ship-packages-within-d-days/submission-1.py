class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        # left = 1
        # right = max(weights) # this is the max weight capacity limit
        weight_cap = float("inf")

        while left <= right:
            mid = left + (right - left) // 2

            # day_count = 0
            day_count = 1
            curr_cap = mid
            for i in range(len(weights)):
                if weights[i] <= curr_cap:
                    curr_cap -= weights[i]
                elif weights[i] > curr_cap:
                    day_count += 1
                    # curr_cap = mid
                    curr_cap = mid - weights[i]

            if day_count > days:
                left = mid + 1
            elif day_count <= days:
                weight_cap = min(mid, weight_cap)
                right = mid - 1


            

        return weight_cap

        
        
        
        
        
        
        # # max weight on one day is capacity of ship
        # # i think we have to binary search based on weights max(weights)to sum(weights)
        # # max(capacity) has to be at elast max(weight)
        # left = max(weights)
        # right = sum(weights)
        # least_weight = float("inf")

        # while left < right:
        #     mid = left + (right - left) // 2

        #     days_needed = 1
        #     curr_load = 0

        #     for weight in weights:
        #         if curr_load + weight > mid:
        #             days_needed += 1
        #             curr_load = weight
        #         else:
        #             curr_load += weight

        #     if days_needed > days:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left



                