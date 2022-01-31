# Python 3.10.1
# Author: Travis Lord
# Purpose:  Show a parent class using normal and abstract methods and a child
# class that inherits functionality from the abstract method in parent
#
#

# importing from abc to access it
from abc import ABC, abstractmethod
class Label(ABC):
    def  labelPrint1(self, size):
        print('Your label size is: ', size)

        @abstractmethod             # abstract method example
        def Measure(self,size):
            pass

class production(Label):            # child class utilizing Measure abstract method 
    def Measure(self,size):
        print(' The label size measured is {} , please configure printer to size.'.format(size))
    def Edit(self):
        print(' Label size does not match box size selected')






if __name__=='__main__':
    lbl = production()           # object instatiation with ref var
    lbl.labelPrint1('6 x 8')      # utilizing regular method through child class
    lbl.Measure('4 x 8')        # utilizing abstract method through child class
    lbl.Edit()                      # child class method utilization 
    
