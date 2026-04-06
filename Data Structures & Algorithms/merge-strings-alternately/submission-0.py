class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        



        pointer1, pointer2 = 0, 0
        output = ""

        while pointer1 < len(word1) and pointer2 < len(word2):
            output += word1[pointer1]
            output += word2[pointer2]
            pointer1 += 1
            pointer2 += 1


        if pointer1 < len(word1):
            output += word1[pointer1:]

        if pointer2 < len(word2):
            output += word2[pointer2:]


        return output
