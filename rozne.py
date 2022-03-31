# from random import shuffle


# lista = ["aa", "bbb", "ccc", "ddd"]


# shuffle(lista)              #tasuje liste

# print("potasowane")
# print(lista)

# last = lista.pop(-1)
# print(last)
# print(lista)


#walrus   z v3.8

# choice = None


# def do_job(choice):
#     print(choice)

# while choice != 0:
#     if (choice := int(input())) != 0:   #  lub  if (choice := int(input()))
#         do_job(choice)



    # choice = int(input())
    # if choice != 0:
    #     do_job(choice)



# class Person:
#     def __init__ (self, name) -> None:
#         self.name = name
#         pass

# luke = Person("luke")
# print(luke.name)
# print(type(luke))



# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.rok = 1
#         print(f"hello {self.name}")
    
#     def __str__(self):
#         return f"hello jestem {self.name}"

#     def promote(self):
#         if self.rok > 4:
#             print("nie da sie dalej")
#         else:
#             self.rok += 1

#     def hello(self):
#         print(f"hello im {self.name}, {self.rok}")

# jan = Student("jan")

# print(jan.name)

# jan.promote()
# jan.promote()
# jan.promote()
# jan.promote()
# jan.promote()
# Student.hello(jan)
# print(jan)



# class Product:
#     def __init__(self, name, netto, vat):
#         self.name = name
#         self.netto = netto
#         self.vat = vat

#     def calculate_brutto(self):
#         return self.netto + self.netto * self.vat

# bread = Product("chleb", 5, 0.23)
# print(bread.calculate_brutto())


# class Aquarium:
#     def __init__ (self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#         self.capacity = self.count()

#     def count(self):
#         return self.width * self.height * self.depth
  

# aqua = Aquarium(100, 20, 30)
# print(aqua.capacity)



# class Aquarium:
#     def __init__ (self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#         self.capacity = self.count(width, height, depth)


#     @staticmethod
#     def count(width, height, depth):
#         return width * height * depth
  

# aqua = Aquarium(100, 20, 30)
# print(aqua.capacity)



# class Aquarium:
#     def __init__ (self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#         self.capacity = self._count(width, height, depth)


#     def _count(self, width, height, depth):
#         return width * height * depth
  

# aqua = Aquarium(100, 20, 30)
# print(aqua._count(10, 20, 30))

"""kompozycja"""


# class Car:
#     def __init__(self, brand, capacity) -> None:
#         self.brand = brand
#         self.engine = Engine(capacity)



# class Engine:
#     def __init__(self, capacity) -> None:
#         self.capacity = capacity


# car = Car("audi", 2.2)
# print(car.engine.capacity)

""""dziedziczenie"""


class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname 

    def hello(self):
        return f"hello im {self.name} {self.surname}"

class Student(Person):
    def __init__(self, name, surname, rok):
        super().__init__(name, surname)
        self.rok = rok

    def promote(self):
        self.rok += 1

class Worker(Person):
    def __init__(self, name, surname, rate) -> None:
        super().__init__(name, surname)
        self.rate = rate
        self.time = 0

    def register_time(self, time):
        self.time += time

    def get_paid(self):
        time = self.time
        self.time = 0
        return time * self.rate

adam = Worker("adam", "kowalski", 100)
print(adam.hello())
adam.register_time(10)
print(adam.get_paid())

    
"""-"""











