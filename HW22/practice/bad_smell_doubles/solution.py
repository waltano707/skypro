class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self, reverse=False):
        return sorted(self.lst, reverse=reverse)


if __name__ == "__main__":
    some_inst = SomeClass()
    print(some_inst.sorted_func())
