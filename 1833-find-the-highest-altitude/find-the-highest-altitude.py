class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAlt = 0

        for g in gain:
            altitude += g
            if altitude > maxAlt:
                maxAlt = altitude

        return maxAlt
        