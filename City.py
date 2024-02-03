class Block:
    def __init__(self, building, x, y):
        self.building = building
        self.x = x
        self.y = y

    def __str__(self):
        return self.building

class City:
    def __init__(self):
        self.blocks = []

    def add_block(self, building, x, y):
        self.blocks.append(Block(building, x, y))

    def __str__(self):
        return '\n'.join([f'{block.building} at ({block.x},{block.y})' for block in self.blocks])
