class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0 

        for sentence in sentences:
            splitted = sentence.split(" ")
            if len(splitted) > output:
                output = len(splitted)

        return output