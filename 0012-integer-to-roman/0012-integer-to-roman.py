class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        sum_ = 0
        nums = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,  "V": 5, "IV": 4, "I": 1}
        
        while sum_ < num:
            max_ = max(nums, key=nums.get)
            if sum_ + nums[max_] <= num:
                sum_ += nums[max_]
                output += max_
            else:
                nums.pop(max_)
        
        return output