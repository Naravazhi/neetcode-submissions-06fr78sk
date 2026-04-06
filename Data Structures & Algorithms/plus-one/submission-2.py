class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if 1 + digits[-1] >= 10:
            carry = 1
            last_digit = (1 + digits[-1]) % 10
        else:
            carry = 0
            last_digit = 1 + digits[-1]
        
        digits[-1] = last_digit

        for i in range(len(digits) - 2, -1, -1):
            currSum = digits[i] + carry
            if currSum >= 10:
                carry = 1
                digits[i] = currSum % 10
            else:
                carry = 0
                digits[i] = currSum
        return [carry] + digits if carry else digits 

