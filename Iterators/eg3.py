class EvenNumbers:
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        self.num += 2
        return self.num
    

evens = EvenNumbers()
even_iter = iter(evens)
while True:
    print(next(even_iter))