class Building:
    def __init__(self, type, width, height, x, y):
        self.type = type
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.type} ({self.width}x{self.height}) at ({self.x},{self.y})'
