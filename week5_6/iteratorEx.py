class FiboSeries:
    def __init__(self,limit):
        self.previous = 0
        self.current = 1
        self.limit = limit
        self.index = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.index += 1
            return result
        else:
            raise StopIteration
    
if __name__ == "__main__":
    r = FiboSeries(100)
    itr = iter(r)
    while True:
        try:
            print(next(itr))
        except StopIteration:
            break