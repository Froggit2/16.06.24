class EvenNumbers:

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.counter_1 = 0
        if self.start is None:
            self.start = 0
        if self.end is None:
            self.end = 1
        if self.start > self.end:
            print('Начало больше конца!')
            pass

    def __iter__(self):
        self.counter_1 = 0
        return self

    def __next__(self):
        for i in range(self.start, self.end):
            self.counter_1 += 1
            if i % 2 == 0:
                continue
            if self.counter_1 >= self.end:
                break


EN = EvenNumbers(10, 25)
for g in range(EN.start, EN.end):
    print(g)