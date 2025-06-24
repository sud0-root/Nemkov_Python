# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed


class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed


my_dog = Dog("Немецкая", 5, "Овчарка")
my_cat = Cat("Вислоухая", 7, "Шотландская")


print(f"Моя собака вида: {my_dog.species}, возрастом: {my_dog.age} лет, породы:  {my_dog.breed}.")
print(f"Моя кошка вида: {my_cat.species}, возрастом: {my_cat.age} лет,  породы: {my_cat.breed }.")