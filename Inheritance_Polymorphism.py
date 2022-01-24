#   Python 3.10.1
#
#   Author: Travis Lord
#
#   Challenge goal:  Create two child classes that use polymorphism from the parent class method.  Each child class having additional attributes 

#parent class 
class Inventory:
    itemClass = 'Electronics'
    itemSource = 'East distribution hub'
    itemMargin = '1%'
    itemDest = 'West warehouse'

    def DataSearch(self):
        response = '\nItem Class: {}\nSource hub: {}\nDestination hub: {}'.format(self.itemClass,self.itemSource,self.itemDest)
        return response
    
#child class
class InventoryCost(Inventory):
    itemClass = 'Electronics'
    itemSource = 'East corporate office'
    itemDest = 'West warehouse'
    itemCost = '$100,000.00'
    itemTransCost = '$1.00'

    def DataSearch(self):
        response = '\nItem Class: {}\nSource hub: {}\nDestination hub: {}\nVendor item Cost: {}\nTransfer Cost: {}'.format(self.itemClass,self.itemSource,self.itemDest,self.itemCost,self.itemTransCost)
        return response
    
#child class
class InventoryShip(Inventory):
    itemClass = 'mounting components'
    itemSource = 'International distribution network'
    itemDest = 'East Distribution Hub'
    itemShip = 'Customer location'
    itemShipCost = '$2.00'
    
    def DataSearch(self):
        response = '\nItem Class: {}\nSource hub: {}\nDestination hub: {}\nCustomer shipment destination: {}\nItem Ship cost: {}'.format(self.itemClass,self.itemSource,self.itemDest,self.itemShip,self.itemShipCost)
        return response 







if __name__=='__main__':
    inv = Inventory()       #object instantiation
    print(inv.DataSearch())     # printing format method used to display the variable information
    
    ICost = InventoryCost()     
    print(ICost.DataSearch()) # using polymorphism to print additional information

    invShp = InventoryShip()
    print(invShp.DataSearch())
