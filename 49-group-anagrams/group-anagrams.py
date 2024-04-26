class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = []
        if len(strs) <= 1:
            output.append(strs)
            return output

        for word in strs:
            group = []
            for word2 in strs:
                if len(word) == len(word2) and sorted(word) == sorted(word2):
                    group.append(word2)

            if group not in output:
                output.append(group)

        output.reverse()
        return output