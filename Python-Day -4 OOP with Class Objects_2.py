=================================================================================================================
#python class called circle with constructor which will take a list as an argument for the task.
#list=[10,501,22,37,100,999,87,351])

import random
import numpy as np

class circle:
    # constructor
    def __init__(self, radius=None, i=10):
        #Initialing arguments with values
        self.pi = 3.141
        self.i = i
        
        #Contional statment to calculate Area and Perimeter of circle
        if radius is None:
            self.r = [random.randint(1, 1000) for _ in range(self.i)]
        else:
            self.r = radius
        self.Area = np.sum(np.array(self.r) ** 2) * self.pi
        self.Perimeter = 2 * self.pi * np.sum(np.array(self.r))
        
#Assigning class into object
circle_obj = circle()
#printing the value of radius,Area and Perimeter of circle
print(circle_obj.r)
print(circle_obj.Area)
print(circle_obj.Perimeter)

#output:
========

#[4, 257, 299, 730, 619, 717, 953, 429, 77, 2]
#8429812.659
#25674.534
=============================================================================================================
#Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
!pip install dataclasses

from dataclasses import dataclass

#decorator from the dataclasses module
@dataclass
#Initializing class
class TV:
    brand: str
    channel: int
    price: int
    inches: int
    ONOFF_status: bool
    volume: int
    #constructor
    def __init__(self, brand, channel, price, inches, ONOFF_status, volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.ONOFF_status = ONOFF_status
        self.volume = volume
#Assigning class into object with keys
tv = TV("Panasonic", 8, 75, 32, True, 75)
print(tv.brand)
print(tv.channel)
print(tv.price)
print(tv.inches)
print(tv.ONOFF_status)
print(tv.volume)




============================================================================================================
#Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV
!pip install dataclasses

from dataclasses import dataclass

#decorator from the dataclasses module
@dataclass
#Initializing parent class 
class TV:
    brand: str
    channel: int
    price: int
    inches: int
    ONOFF_status: bool
    volume: int
    
#Inheriting child class with additional properties
class Child(TV):
    thickness: int
    energy_usage: int
    lifespan: int
    refresh_rate: int
    viewingAngle:int 
    Backlight: str
    DisplayDetails:str
    
    #Initializing method with arguments
    def __init__(self, brand, channel, price, inches, ONOFF_status, volume,thickness,energy_usage,lifespan,refresh_rate,viewingAngle,Backlight,DisplayDetails):
        super().__init__(brand, channel, price, inches, ONOFF_status, volume)
        self.thickness=thickness
        self.energy_usage=energy_usage
        self.lifespan=lifespan
        self.refresh_rate=refresh_rate
        self.viewingAngle=viewingAngle
        self.Backlight=Backlight
        self.DisplayDetails=DisplayDetails
        
#Assigning class into object with keys
tv_child = Child("Panasonic", 8, 75, 32, True, 75,32,10,5,2,360,"white","oval")
print(tv_child.brand)
print(tv_child.channel)
print(tv_child.price)
print(tv_child.inches)
print(tv_child.ONOFF_status)
print(tv_child.volume)
print(tv_child.thickness)
print(tv_child.energy_usage)
print(tv_child.lifespan)
print(tv_child.refresh_rate)
print(tv_child.viewingAngle)
print(tv_child.Backlight)
print(tv_child.DisplayDetails)

