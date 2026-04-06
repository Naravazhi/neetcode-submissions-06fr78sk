class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_array = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            word_array[index] += 1

        for i in range(len(t)):
            index = ord(t[i]) - ord('a')
            if word_array[index] == 0:
                return False
            word_array[index] -= 1

        for i in range(len(word_array)):
            if word_array[i] > 0:
                return False
        return True



