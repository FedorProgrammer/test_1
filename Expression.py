class Expression:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def calc(self):
        return 0