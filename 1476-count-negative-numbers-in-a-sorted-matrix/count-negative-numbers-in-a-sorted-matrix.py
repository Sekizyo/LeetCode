class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] < 0:
                    count += 1

        return count