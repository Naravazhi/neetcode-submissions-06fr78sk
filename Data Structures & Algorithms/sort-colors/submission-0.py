class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        

        for i in range(len(nums)):
            arr[nums[i]] += 1
            # if nums[i] == 0:
            #     arr[0] += 1
            # elif nums[i] == 1:
            #     arr[1] += 1
            # else:
            #     arr[2] += 1
        index = 0
        while index < arr[0]:
            nums[index] = 0
            index +=1 
        while index < arr[0] + arr[1]:
            nums[index] = 1
            index += 1
        while index < arr[0] + arr[1] + arr[2]:
            nums[index] = 2
            index += 1
            




