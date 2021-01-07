class Buffer:
    def __init__(self):
        self.arr = []


    def add(self, *a):
        self.arr.extend(a)
        while len(self.arr) >= 5:
            print(sum(self.arr[:5]))
            del self.arr[0:5]

    def get_current_part(self):
        print(self.arr)
        return self.arr