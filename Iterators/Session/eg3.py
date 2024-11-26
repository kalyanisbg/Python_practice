class EvenNumbers:
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if self.num < 10:
            self.num += 2
            return self.num
        else:
            raise StopIteration
    

evens = EvenNumbers()
even_iter = iter(evens) 
while True:
    print(next(even_iter))