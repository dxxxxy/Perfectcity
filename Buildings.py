class Building:
    def __init__(self, type, width, height, x = 0, y = 0):
        self.type = type
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.type} ({self.width}x{self.height}) at ({self.x},{self.y})'

house = Building("house", 1, 1)

grocery_store = Building("grocery store", 1, 2)
drug_store = Building("drug store", 1, 1)
park = Building("park", 3, 3)
library = Building("library", 2, 2)
school = Building("school", 3, 4)
