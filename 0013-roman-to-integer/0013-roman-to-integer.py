class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {"0": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0
        i = 0
        s+="0"
        while i < len(s)-1: 
            a = nums[s[i]]
            b = nums[s[i+1]]
            if a < b:
                output += b-a
                i += 1
            else:
                output += a
            i += 1

        return output