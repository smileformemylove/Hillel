class Auto:

    def __init__(self, brand, age, mark, color = True, weight = 2500):
        self.brand = brand
        self.__color = color
        self.age = age
        self.mark = mark
        self.__weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(self.age)

my_car = Auto("audi", 12, "A8" )
print(my_car.age)
print(my_car.brand)
print(my_car.mark)
# print(my_car.__dict__)
my_car.birthday()
my_car.move()
my_car.stop()



# print("^" * 50)
# my_car_1 = auto
# my_car_1.brand = "BMW"
# my_car_1.age = 5
# my_car_1.mark = 328
# print(my_car_1.brand)
# print(my_car_1.age)
# print(my_car_1.mark)




