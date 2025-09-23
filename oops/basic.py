#basic class and object
#if we want to make any attribute private we use __ before the attribute name
#inheritance    
#super() function is used to give access to the parent class methods and attributes
#encapsulation  
#getter method is used to access the private attribute of a class
class Car:
    total_cars=0
    def __init__(self,userbrand,usermodel):
        self.__brand= userbrand
        self.__model= usermodel
        Car.total_cars +=1


    def get_brand(self):
        return self.__brand+ "!"
    
    def full_name(self):
        print(f"{self.__brand} {self.__model}")

    def Fuel_type(self):
        return "Petrol or disal"
    
    @staticmethod
    def general_info():
        return "This is a car"
    
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery):
        super().__init__(userbrand,usermodel)
        self.battery=battery

    def car_battery(self):
        print(f"{self.brand} {self.__model} has a battery of {self.battery} kWh")
    
    def Fuel_type(self):
        return "Electricity"


# my_tesla = ElectricCar("tesla","model 3",75)
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar)) #True


#my_tesla.model = "model Y"

# print(my_tesla.model()) 
#output: model Y
# so we need to stop this from happening 


# print(my_tesla.get_brand())
# my_tesla.full_name()
# my_tesla.car_battery()   
# 
# print(my_tesla.Fuel_type())   
# print(my_tesla.general_info())



# my_car = Car("maruti","800")
# print(my_car.brand)
# print(my_car.model)
# my_car.full_name()    
# print(my_car.Fuel_type())

# to find total cars
 
# print(Car.total_cars)

class Bike:
    def battery(self):
        return "12V"
class Truck:
    def Engine(self):
        return "24V"
class Engine(Bike,Truck,Car):
    pass

my_new_tesla = Engine("tesla","model X")
print(my_new_tesla.battery())  #12V