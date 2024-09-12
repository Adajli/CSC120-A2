class ResaleShop:

    # What attributes will it need?
    item_id: int
    new_price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, item_id: int, new_price:int):
        self.item_id = item_id  
        self.new_price = new_price
    

    # What methods will you need?
    def updatePrice(self,new_price:int):
        self.new_price = new_price
    