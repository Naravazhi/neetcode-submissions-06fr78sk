class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # when we see character we want to know where the last instance of it is
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        size = 0
        end = 0
        res = []

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res



