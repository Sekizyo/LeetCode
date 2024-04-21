class Solution:
    def Extract(self, lst: list[str], i: int) -> list[str]:
        return [item[i] for item in lst]
    
    def check(self, lst:list[str]) -> bool:
        dict_ = {}
        for word in lst:
            if not word in dict_.keys():
                dict_[word] = 1
            else:
                dict_[word] += 1
            
        if len(dict_.keys()) == 1:
            return True
        return False

    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLen = len(strs[0])
        for word in strs:
            if len(word) < minLen:
                minLen = len(word)
                
                
        output = ""
        for i in range(minLen):
            list_ = self.Extract(strs, i)
            if self.check(list_):
                output += strs[0][i]
            else:
                break
        
        return output