class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start - 1
        self.end = end
        if self.start > self.end:
            raise StopIteration("Начало больше конца!")

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start % 2 == 0:
            return self.start
        if self.start >= self.end:
            raise StopIteration


EN = EvenNumbers(10, 25)
for num in EN:
    if num is None:
        continue
    print(num)