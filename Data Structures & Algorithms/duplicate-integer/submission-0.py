class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = 1
        return False






        
        
        
        
        
        
        
        
        
        # hashset = set()

        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False