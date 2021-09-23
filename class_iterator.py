class TopTwenty:
    def __init__(self,count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 10:
            var = self.count
            self.count += 1
            return var
        else:
            raise StopIteration
        

    
values = TopTwenty(1)
for i in values:
    print(i)