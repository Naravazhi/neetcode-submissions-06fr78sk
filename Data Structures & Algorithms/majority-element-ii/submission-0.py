class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        count = {}
        n = len(nums)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > n // 3 and num not in res:
                res.add(num)
        return list(res)
