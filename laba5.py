import random

class Furniture:
    def __init__(self, name, x, y):
        self.name = name
        self.coordinates = [x, y]

    def move(self, new_x, new_y):
        old_coordinates = self.coordinates.copy()
        self.coordinates = [new_x, new_y]
        return old_coordinates 

    def __str__(self):
        return f"{self.name} at {self.coordinates}"


class Bed(Furniture):
    def __init__(self, x, y):
        super().__init__("Bed", x, y)


class Sofa(Furniture):
    def __init__(self, x, y):
        super().__init__("Sofa", x, y)


class Table(Furniture):
    def __init__(self, x, y):
        super().__init__("Table", x, y)


class Carpet(Furniture):
    def __init__(self, x, y):
        super().__init__("Carpet", x, y)


class Room:
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
            new_x = random.randint(0, 100)
            new_y = random.randint(0, 100)
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


def main():
    room = Room()  
    bed = Bed(10, 15)
    sofa = Sofa(20, 25)
    table = Table(30, 35)
    carpet = Carpet(5, 10)

    room.add_furniture(bed)
    room.add_furniture(sofa)
    room.add_furniture(table)
    room.add_furniture(carpet)

    print("Initial furniture arrangement:")
    print(room) 

    print("\nRearranging furniture to new random coordinates:")
    room.rearrange()  

    print("\nNew furniture arrangement:")
    print(room)  

main()
