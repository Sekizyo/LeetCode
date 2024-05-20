class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = {}

        for ID, groupID in enumerate(groupSizes):
            if not groupID in groups.keys():
                groups[groupID] = [ID]
            else:
                groups[groupID].append(ID)

        output = []
        for key, value in groups.items():
            for i in range(0, len(value), key):
                output.append(groups[key][i:i+key])

        return output