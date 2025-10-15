#this are class
class car:
    def __init__(car,color,brand): #constructor
        car.color = color
        car.brand = brand

    def  drive(car):
        print(f"{car.brand} is driving on road whose color is {car.color}")      

#this is an object
car1 = car("red","mustang")

#calling an object
car1.drive()