class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDict = {}
        
        for num in nums:
            if not num in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
                
        nums.clear()
        
        for key, num in numDict.items():
            print(key, num)
            if num > 2:
                num = 2
            for _ in range(num):
                nums.append(key)
                
        return len(nums)
        