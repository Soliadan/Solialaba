import random
from random import randint

class Furniture():
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.coordinates = [x, y]
        self.width = width
        self.height = height
        self.bottom_right = [x + width - 1, y + height - 1]

    def move(self, new_x, new_y):
        old_coordinates = self.coordinates.copy()
        self.coordinates = [new_x, new_y]
        self.bottom_right = [new_x + self.width - 1, new_y + self.height - 1]
        return old_coordinates 

    def get_positions(self):
        
        positions = []
        for dx in range(self.width):
            for dy in range(self.height):
                positions.append([self.coordinates[0] + dx, self.coordinates[1] + dy])
        return positions

    def __str__(self):
        return f"{self.name} at {self.coordinates} with size ({self.width}x{self.height})"


class Bed(Furniture):
    def __init__(self, x, y):
        super().__init__("Bed", x, y, width=2, height=3)  

class Sofa(Furniture):
    def __init__(self, x, y):
        super().__init__("Sofa", x, y, width=2, height=2) 

class Table(Furniture):
    def __init__(self, x, y):
        super().__init__("Table", x, y, width=1, height=2)  


class Carpet(Furniture):
    def __init__(self, x, y):
        super().__init__("Carpet", x, y, width=3, height=3)  


class Room():
    def __init__(self):   
        self.furniture_list = []

    def add_furniture(self, furniture):
        self.furniture_list.append(furniture)
        print(f"{furniture.name} added in room at position: {furniture.coordinates}")

    def remove_furniture(self, furniture_name):
        for furniture in self.furniture_list:
            if furniture.name == furniture_name:
                self.furniture_list.remove(furniture)
                print(f"{furniture.name} removed from the room.")
                return
        print(f"{furniture_name} is not in the room.")

    def rearrange(self):
        for furniture in self.furniture_list:
            new_x = random.randint(5, 25)
            new_y = random.randint(5, 25)
            old_coordinates = furniture.move(new_x, new_y)
            print(f"{furniture.name} moved from {old_coordinates} to {furniture.coordinates}")

    def show_furniture(self):
        if not self.furniture_list:
            print("The room is empty.")
        else:
            for furniture in self.furniture_list:
                print(furniture)
    
    def __str__(self):
        if not self.furniture_list:
            return "The room is empty."
        else:
            return "Furniture in the room:\n" + "\n".join(str(furniture) for furniture in self.furniture_list)


def drawroom(*args):
    space = [["  " for _ in range(30)] for _ in range(30)]
    statements = []

  
    for i in range(2, 28):
        space[i][2] = "- "
        space[i][28] = "- "
    for i in range(2, 29):
        space[2][i] = "| "
        space[28][i] = "| "

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for rooms in args:
        for fur in rooms.furniture_list:
            symbol = alphabet[randint(0, len(alphabet) - 1)]
            alphabet.remove(symbol)
            symbol += " "
            for pos in fur.get_positions():
                x, y = pos
                if 0 <= x < 30 and 0 <= y < 30:
                    if space[x][y] == "  ":
                        space[x][y] = symbol
                    else:
                        statements.append(f"Conflict: {fur.name} at position {x}, {y} is overlapping with {space[x][y].strip()}.")


    for i in range(30):
        print("".join(space[j][i] for j in range(30)))
    
   
    for statement in statements:
        print(statement)

def main():
    room = Room()  

    bed = Furniture("Bed", 10, 15, width=2, height=3)
    sofa = Furniture("Sofa", 20, 25, width=2, height=2)
    table = Furniture("Table", 15, 15, width=1, height=2)
    carpet = Furniture("Carpet", 5, 10, width=3, height=3)


    room.add_furniture(bed)
    room.add_furniture(sofa)
    room.add_furniture(table)
    room.add_furniture(carpet)

    print("Initial furniture arrangement:")
    print(room) 

    print("Rearranging furniture to new random coordinates:")
    room.rearrange()  

    print("New furniture arrangement:")
    print(room)
    drawroom(room)

main()
