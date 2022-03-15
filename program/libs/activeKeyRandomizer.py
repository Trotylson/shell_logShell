import random

class Randomizer():
    
    def __init__(self):
        self.key = ''
        
    def generateKay(self):
        for x in range(0,6):
            self.key += str(random.randint(0, 9))
        return self.key
    
    def keyApprove(self, given):
        if given == self.key:
            return True
        return False