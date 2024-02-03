import tkinter as tk
import random

class Building:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False

def generate_city(num_buildings):
    buildings = []
    for _ in range(num_buildings):
        x = random.randint(10, 400)
        y = random.randint(10, 400)
        width = random.randint(20, 100)
        height = random.randint(50, 200)
        buildings.append(Building(x, y, width, height))
    return buildings

def draw_city(buildings):
    canvas.delete("all")
    for building in buildings:
        fill_color = "gray" if not building.selected else "blue"
        canvas.create_rectangle(
            building.x,
            building.y,
            building.x + building.width,
            building.y + building.height,
            fill=fill_color,
            tags=str(building),
        )

def on_building_click(event):
    x, y = event.x, event.y
    clicked_item = canvas.find_closest(x, y)
    building_id = canvas.gettags(clicked_item)[0]

    for building in buildings:
        building.selected = building_id == str(building)

    draw_city(buildings)
    canvas.tag_raise(str(building_id))  # Bring the selected building to the front

def on_building_drag(event):
    x, y = event.x, event.y
    for building in buildings:
        if building.selected:
            building.x = x - building.width / 2
            building.y = y - building.height / 2

    draw_city(buildings)

def generate_and_draw_city():
    global buildings
    num_buildings = int(entry.get())
    buildings = generate_city(num_buildings)
    draw_city(buildings)
    for building in buildings:
        canvas.tag_bind(str(building), "<Button-1>", on_building_click)
        canvas.tag_bind(str(building), "<B1-Motion>", on_building_drag)

# GUI setup
root = tk.Tk()
root.title("City Simulation")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

label = tk.Label(root, text="Number of Buildings:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate City", command=generate_and_draw_city)
button.pack()

buildings = []

root.mainloop()
