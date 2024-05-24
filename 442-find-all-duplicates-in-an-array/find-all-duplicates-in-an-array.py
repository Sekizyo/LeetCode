class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numsDict = {}

        for num in nums:
            if num not in numsDict.keys():
                numsDict[num] = 1
            else:
                numsDict[num] += 1

        duplicates = []
        for key, value in numsDict.items():
            if value > 1 and key not in duplicates:
                duplicates.append(key)

        return duplicates
        