class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded


    def decode(self, s: str) -> List[str]:

        i = 0
        curr_str = ""
        res = []
        while i < len(s):
            # 4#home6#nannan
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            curr_str = s[i:i + length]
            res.append(curr_str)
            i += length

            # if s[index].isdigit():
            #     res.append(curr_str)
            #     curr_str = s[index: index + int(s[index])]
            #     index += int(s[index])
                
        return res
                

                
            


