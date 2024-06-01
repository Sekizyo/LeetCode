class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letterCount = {}
        for letter in s:
            if letter not in letterCount.keys():
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1

        if len(list(set(list(letterCount.values())))) == 1:
            return True
        return False 
        