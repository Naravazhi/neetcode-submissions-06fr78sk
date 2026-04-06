class Solution:


    def encode(self, strs: List[str]) -> str:
        big_str = ""
        for s in strs:
            big_str += str(len(s)) + "#" + s
        return big_str

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res





        # res = []

        # i = 0

        # while i < len(s):
        #     j = i
        #     while s[j] != "#":
        #         j += 1
        #     length = int(s[i:j])
        #     i = j + 1
        #     j = i + length
        #     res.append(s[i:j])
        #     i = j


        # return res

        #    4#neet4#code4#love3#you
