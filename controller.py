from oop.miner.field import Field
from oop.miner.view import View

class Controller:
    def __init__(self):
        self.field = Field()
        self.field.generate_field()
        self.view = View(self.field)
        x = int(input())
        y = int(input())
        self.field.open_cell(x, y)
        self.view.display_field()

    def start_game(self):
        self.field.open_cell(1, 1)
        self.view.display_field()


ctrl = Controller()
