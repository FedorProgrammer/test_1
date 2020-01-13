from oop.miner.field import Field


class View:
    def __init__(self, field: Field):
        self.field = field # type: oop.miner.Field

    def display_field(self):
        pass

    def get_user_turn(self):
        pass