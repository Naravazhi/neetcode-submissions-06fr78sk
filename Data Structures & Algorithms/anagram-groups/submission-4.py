class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        hashmap = {}

        for string in strs:
            key = sorted(string)
            key = "".join(key)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
            
        # for x in hashmap.items():
        #     ans.append(list(x))
        for key, value in hashmap.items():
            ans.append(value)

        return ans