class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        multiplier = 1
        for i in range(len(digits) - 1, -1, -1):
            number += digits[i] * multiplier
            multiplier = multiplier * 10
        
        number += 1
        result = [int(d) for d in str(number)]
        return result



