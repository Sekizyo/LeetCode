class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        for num in arr:
            if not num in count.keys():
                count[num] = 1
            else:
                count[num] += 1
        
        occurrences = list(count.values())
        occurLen = len(occurrences)
        if len(set(occurrences)) == occurLen:
            return True
        return False