class Solution:
    def likeTimeCoefficient(self, satisfaction: list[int]) -> int:
        output = 0
        for i, sat in enumerate(satisfaction):
            output += sat*(i+1)
        return output

    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction = sorted(satisfaction)
        oldMax = 0

        for i in range(len(satisfaction)):
            newMax = self.likeTimeCoefficient(satisfaction[i:])
            if newMax > oldMax:
                oldMax = newMax 

        if oldMax <= 0:
            return 0

        return oldMax