from random import randint
class RandomizedSet:

    def __init__(self):
        self.output = []

    def insert(self, val: int) -> bool:
        if not val in self.output:
            self.output.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.output:
            self.output.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.output[randint(0, len(self.output)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()