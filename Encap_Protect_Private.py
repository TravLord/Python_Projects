# Python 3.10.1
# Author: Travis Lord
# Challenge Details: Make use of private and protected variables within a class
#

# protected variable example
class First_protect:
    def __init__(self):
        self._PVar =0

# private variable example
class Second_Private:
    def __init__(self):
        self.__PvVar = 49

    def getter(self):
        return self.__PvVar

    def setter(self, private):
        self.__PvVar = private













if __name__=='__main__':
    Temp1 = First_protect()     # object making use of protected variable through print method
    Temp1._PVar =77
    print(Temp1._PVar)

    Pct = Second_Private()    # object making use of private variable through print method
    Pct.getter()
    Pct.setter(88)
    print(Pct.getter())
    
    
