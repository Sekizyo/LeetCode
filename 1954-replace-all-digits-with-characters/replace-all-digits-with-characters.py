class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ""
        for i in range(0, len(s)-1, 2):
            letter = s[i]
            output += letter
            output += chr(ord(letter) + int(s[i+1]))
        
        if (len(s)-1) % 2 == 0:
            output += s[-1]

        return output