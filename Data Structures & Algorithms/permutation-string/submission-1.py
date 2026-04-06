class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False
        

        s1Counts = [0] * 26
        winCounts = [0] * 26

        for i in range(m):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            s1Counts[idx1] += 1
            winCounts[idx2] += 1

        if s1Counts == winCounts:
            return True
        

        left = 0
        for right in range(m, n):
            # i to i + len(s1)
            # for i in range(right, right + len(s1)):
            #     if s1Counts[s2[i]] != s2Counts[s2[j]]:
            #         right += 1
            #         break
            addIdx = ord(s2[right]) - ord('a')
            winCounts[addIdx] += 1
            removeIdx = ord(s2[left]) - ord('a')
            winCounts[removeIdx] -= 1
            left += 1
            

            if s1Counts == winCounts:
                return True

        return False

                




            




