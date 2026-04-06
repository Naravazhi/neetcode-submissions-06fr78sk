class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        stack = []

        for i in range(len(s)):
            stack.append(s[i])

        for i in range(len(stack)):
            s[i] = stack.pop()


        # def reverse(l, r):
        #     if l < r:
        #         reverse(l + 1, r - 1)
        #         s[l], s[r] = s[r], s[l]



        


        # reverse(0, len(s) - 1)
        

        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     temp = s[left]
        #     s[left] = s[right]
        #     s[right] = temp
        #     left += 1
        #     right -= 1
        