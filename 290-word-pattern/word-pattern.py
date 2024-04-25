class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) < len(s.split(" ")):
            return False

        count = {}
        for i, word in enumerate(s.split(" ")):
            if word not in count.keys():
                count[word] = pattern[i]

        output = ""
        for char in pattern:
            output += self.get_key(count, char) + " "

        
        if output[:-1] == s:
            return True
        return False
    
    def get_key(self, dict_: dict[str], val: str) -> str:
        for key, value in dict_.items():
            if val == value:
                return key
        return ""