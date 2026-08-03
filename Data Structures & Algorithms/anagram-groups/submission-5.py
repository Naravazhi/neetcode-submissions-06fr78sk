class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        anagram_map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagram_map:
                anagram_map[sorted_string] = [string]
            else:
                anagram_map[sorted_string].append(string)
        
        for key, value in anagram_map.items():
            ans.append(value)
        return ans







        return ans









        # ans = []

        # hashmap = {}

        # for string in strs:
        #     key = sorted(string)
        #     key = "".join(key)
        #     if key in hashmap:
        #         hashmap[key].append(string)
        #     else:
        #         hashmap[key] = [string]
            
        # # for x in hashmap.items():
        # #     ans.append(list(x))
        # for key, value in hashmap.items():
        #     ans.append(value)

        # return ans