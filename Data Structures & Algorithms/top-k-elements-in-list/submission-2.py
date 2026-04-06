# class Solution:
#     def topKElements(self, nums: List[int], k: int) -> List[int]:


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [4, 5, 6, 2, 3, 4, 5, 6, 8, 4]
        # have a hashmap with integer values 
        # key is num : value is count
        # then we have to sort by values then pop by k

        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        

        pairs = []
        for key, value in count.items():
            pairs.append((key, value))
        
        sorted_values = sorted(pairs, key=lambda x:x[1])

        b = len(sorted_values) - 1
        while k:
            num, cnt = sorted_values[b]
            res.append(num)
            k -= 1
            b -= 1

        return res








# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:























        

        # # coutns of each number
        # counts = {}
        # for num in nums:
        #     counts[num] = 1 + counts.get(num, 0)


        # buckets = [[] for _ in range(len(nums) + 1)]
        # for num, freq in counts.items():
        #     buckets[freq].append(num)


        # ans = []
        # j = 0

        # for f in range(len(nums), 0, -1):
        #     for num in buckets[f]:
        #         ans.append(num)
        #         j += 1
        #         if j == k:
        #             return ans

