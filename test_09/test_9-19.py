class Counter:
    def reset(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

    def get(self):
        return self.count
    
a = Counter()
b = Counter()

a.reset()
b.reset()

a.increment()
a.increment()
print("카운트 a의 값은?", a.get())

b.increment()
print("카운트 b의 값은?", b.get())