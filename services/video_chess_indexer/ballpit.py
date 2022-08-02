class Test:
    def __init__(self, val = 1):
        self.val = val

    def show(self):
        print(self.val)

my_list = []

obj = Test()
obj = None

print(obj.val)