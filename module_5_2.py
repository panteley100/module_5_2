class House:

    def __init__ (self,name, number_of_floors):
        self.__str__ (name, number_of_floors)
        self.__len__(number_of_floors)

    def __str__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print('Название:', self.name, 'Кол-во этажей:', self.number_of_floors)

    def __len__ (self, number_of_floors):
        self.number_of_floors = number_of_floors
        print('Кол-во этажей:',self.number_of_floors)

h1 = House ('ЖК Эльбрус', 10)
h2 = House ('ЖК Акация', 20)