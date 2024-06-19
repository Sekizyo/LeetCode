class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCount = 0
        maxIndex = 0
        for i, row in enumerate(mat):
            count = row.count(1)
            if count > maxCount:
                maxCount = count
                maxIndex = i

        return [maxIndex, maxCount]

        