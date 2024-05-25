class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output = []
        for centerX, centerY, radius in queries:
            count = 0
            for x, y in points:
                if abs(x-centerX)**2 + abs(y-centerY)**2 <= radius**2:
                    count += 1
            output.append(count)

        return output