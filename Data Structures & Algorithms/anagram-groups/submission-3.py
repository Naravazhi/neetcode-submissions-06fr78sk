class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # key: value should be sorted word : list of unsorted words
        # for each string in the strings array we need to sort then 
        # if a new "key" encountered add to the hashmap
        # ways we could: hashmap, array of chars
        res = []
        hashmap = {} # str : List[str]
        for str in strs:
            # key = sorted(str)
            # key = str.sort()
            key = "".join(sorted(str))
            if key not in hashmap:
                # add to the hashmap
                hashmap[key] = [str]
            else:
                hashmap[key].append(str)
            
        for key, value in hashmap.items():
            res.append(value)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = defaultdict(list)

        # for word in strs:
        #     count = [0] * 26
        #     for c in word:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(word)
        # return list(res.values())
        
        # groups = {}
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     if key in groups:
        #         groups[key].append(word)
        #     else:
        #         groups[key] = [word]

        # return list(groups.values())
        
        
        # hashmap = defaultdict(list)
        # output = []

        # for word in strs:
        #     sorted_word = word.sort()
        #     if sorted_word in hashmap:
        #         hashmap[sorted_word].append(word)
        #     else:
        #         hashmap[sorted_word] = [word]
        # return output

    # def isValid(self, str: word1, str: word2) -> bool:
    #     if len(word1) != len(word2):
    #         return False

    #     word_array = [0] * 26

    #     for i in range(len(word1)):
    #         word_array[ord(word1[i]) - ord('a')] += 1
    #         word_array[ord(word2[i]) - ord('a')] -= 1
        
    #     for i in range(len(word_array)):
    #         if word_array[i] == 0:
    #             return False
    #         word_array[i] -= 1
    #     return True

