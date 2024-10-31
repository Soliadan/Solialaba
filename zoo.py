class Zoo:
    tickets : int 

    # def __init__(self, visitors, name, number_of_animals, location, tickets):
    def __init__(self, visitors=0, name="", number_of_animals=0, location="", tickets=0.0, pay=0):
        self.__visitors = visitors
        self.__name = name
        self.__number_of_animals = number_of_animals
        self.location = location
        self.tickets = tickets
        self.__pay = pay

    def __str__(self):
        return (f"Zoo info:\n"
                f"(Visitors: {self.__visitors})\n"
                f"(Name: {self.__name})\n"
                f"(Number_of_animals: {self.__number_of_animals})\n"
                f"(Location: {self.location})\n"
                f"(Tickets: {self.tickets})\n")
                
    def __repr__(self):
        return (f"Visitors='{self.__visitors}', "
                f"Name={self.__name}, "
                f"Number_of_animals={self.__number_of_animals}, "
                f"Location={self.location}, "
                f"Tickets={self.tickets} ")
              

    def get_visitors(self):
        return self.__visitors

    def get_number_of_animals(self):
        return self.__number_of_animals

    def get_name(self):
        return self.__name

    def set_visitors(self, visitors):
        self.__visitors = visitors

    def set_number_of_animals(self, number_of_animals):
        self.__number_of_animals = number_of_animals

    
    def set_number_of_animals (self, number_of_animals):
        if number_of_animals >= 0:
            self.__number_of_animals  = number_of_animals 
        else:
            print("ValueError")

    
    
    def set_pay(self, pay):
        self.__pay = pay
    
    def get_pay(self):
        return self.__pay
    
    
    def set_name(self, name):
        self.__name = name

    def __del__(self):
        print("Object deleted")
    
    
def minPayCount(zoo_list):
    minZoo = zoo_list[0]
    for zoo in zoo_list :
        if zoo.get_pay() < minZoo.get_pay():
           minZoo = zoo
    return minZoo





    
def main():
    zoo_1 = Zoo(77, "Відморожений", 100, "Самбір", 1000, 100)
    zoo_2 = Zoo(82, "Лапка", 120, "Рахів", 1200, 100)
    zoo_3 = Zoo(97, "Вусик", 220, "Калуш", 1500, 11)
    zoo_4 = Zoo(97, "Вусик33", 220, "Калуш", 1000, 50)


    # zoo_3.set_number_of_animals("hello")
    
  
    # print(zoo_1)
    # print(zoo_2)
    # print(zoo_3)
    # print(zoo_4)

    print( minPayCount([zoo_1, zoo_2, zoo_3, zoo_4]) )

    zoo_3.set_pay(1000)

    print( minPayCount([zoo_1, zoo_2, zoo_3, zoo_4]) )


if __name__ == "__main__":
    main()
