class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)

        return output
        