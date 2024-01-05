class Id:
    def __init__(self):
        self.num = 0
    
    def nextId(self):
        self.num +=1
        return self.num - 1