class ThreadStatic:
    def __init__(self):
        self.Done = False

    def Status (self):
        return self.Done

    def Stop (self):
        self.Done = True