class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            nums[left] = nums[right]
            while right < n and nums[right] == nums[left]:
                right += 1
            left += 1
        return left



        

        

        # pointer = len(nums) - 2
        # for i in range(len(nums) - 1, -1, -1):

        #     while nums[pointer] == nums[i]:
        #         nums[pointer] = 0
        #         pointer -= 1
            
        # count = 0
        # for num in nums:
        #     if :
        #         count += 1
        # return count