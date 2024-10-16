from typing import Any


class Computer:

    # What attributes will it need?
    description: str = "<NO DESC AVAILABLE>"
    processor_type: str
    hard_drive_capacity: int
    memory: int = 0
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self. operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need? 
    'Saves attributes of the computer by printing them.'
    def attributes(self):
        return vars(self)
    'Allows input of updating the OS.'
    def updateOS(self,operating_system):
        self.operating_system = operating_system
    'Allows input of updating the price.'
    def updatePrice(self,price:int):
        self.price = price
    # Updates year
    def updateYear(self, year_made):
        self.year_made = self.year_made +1
    # Get year
    def getYear(self,year_made):
        return self.year_made
    def __str__(self) -> str:
        return "Desc:" + self.description + "\n" + "Processor:" + self.processor_type + "\n"+ "HD Capacity:" + str(self.hard_drive_capacity) + "\n"+ "Memory:" + str(self.memory) + "\n"+ "Operating System:" + self.operating_system + "\n" + "Year Made:" + str(self.year_made) + "\n"+ "Price:" + str(self.price) + "\n"

def main():
        my_computer = Computer(
            "Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500
        )    
        #my_computer.updatePrice(150)
        #my_computer.updateYear(my_computer.getYear())
        #my_computer.updateOS("macOS Ventura 13.6 ")
        print(my_computer.__str__())
        print(my_computer.attributes())

main()
