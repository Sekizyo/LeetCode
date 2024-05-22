class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph = {}
        for s in sentence:
            if s not in alph.keys():
                alph[s] = 1
        
        if len(alph.keys()) >= 26:
            return True
        return False
        