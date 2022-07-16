class name():
    def __init__(self):
        self.name = ["Ram","Shyam","Sita","Gita"]
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.name):
            raise StopIteration
        
        return self.name[self.index]

n = name()
itr = iter(n)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))