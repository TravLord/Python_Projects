#   Python: 3.10.1
#   Author: Travis Lord
#   Assignment Details:   Creating Parent Class with two children that inherit its attributes
#


class Vehicle:
    model: ""
    engine = ""
    bodyType = ""
    year = ""
    color = ""
    weight = ""
    
    def __init__(self,model,engine,bodyType,year,color,weight):
         self.model = model
         self.engine = engine
         self.bodyType = bodyType
         self.year = year
         self.color = color
         self.weight = weight
        

New_Vehicle = Vehicle("Tesla X","Electric","Sedan","2019","Black","2400lbs")

from pprint import pprint
pprint(vars(New_Vehicle))

class Plane(Vehicle):
    wingLength = ""
    faaID = ""

    def __init__(self,model,engine,bodyType,year,color,weight,wingLength,faaID):
         self.model = model
         self.engine = engine
         self.bodyType = bodyType
         self.year = year
         self.color = color
         self.weight = weight
         self.wingLength = wingLength
         self.faaID = faaID
New_Plane = Plane("Boeing","Combustion","737","2010","white","50,000lbs","40ft","98789")

from pprint import pprint
pprint(vars(New_Plane))



class Car(Vehicle):
    LPlateNum = ""
    RegYear = ""
    
    
