class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #groups = {}
        # groups = defaultdict(list)

        # for str in strs:
        #     count = [0] * 26
        #     for c in str:
        #         count[ord(c) - ord("a")] += 1
        #     groups[tuple(count)].append(str)
        # return list(groups.values())
        groups = defaultdict(list)

        # lists arent hashable so use tuple so you can make it a key
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())

       
       
        
       
       
       
       
       
       
       
       
       
       
       
       
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        # return list(res.values())