class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        paied = 0
        costs = sorted(costs)
        
        for cost in costs:
            if paied + cost <= coins:
                count += 1
                paied += cost

        return count