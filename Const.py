from oop.Expression.Expression import Expression


class Const(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value