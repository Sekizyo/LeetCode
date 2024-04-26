class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for char in s:
            if char not in sDict.keys():
                sDict[char] = 1 
            else:
                sDict[char] += 1

        for char in t:
            if char not in tDict.keys():
                tDict[char] = 1 
            else:
                tDict[char] += 1

        for char in t:
            if not char in sDict.keys():
                return False

            if sDict[char] > tDict[char]:
                return False
        
        return True