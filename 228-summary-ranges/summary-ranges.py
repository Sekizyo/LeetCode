class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        
        if len(nums) == 1:
            return [f"{nums[0]}"]
        ranges = [] 
        i = 0

        newRange = [nums[0]]
        
        while newRange[-1] != nums[-1]:
            num1 = nums[i]

            newRange = [num1]
            newRangeIndex = [i]
            
            for num2 in nums[i+1:]:
                if num2 - newRange[-1] == 1:
                    newRange.append(num2)  
                    newRangeIndex.append(nums.index(num2))
                else:
                    i = newRangeIndex[-1] + 1
                    break
            
            if len(newRange) == 1:
                ranges.append(f"{num1}")
            else:
                ranges.append(f"{num1}->{newRange[-1]}")

        return ranges