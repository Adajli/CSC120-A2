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
    def storeInformation(self, description:str, processor_type:str, hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        description = self.description 
        processor_type = self.processor_type
        hard_drive_capacity = self.hard_drive_capacity
        memory = self.memory
        operating_system = self.operating_system
        year_made = self.year_made
        price == self.price
        print(description, processor_type,hard_drive_capacity,memory,operating_system,year_made,price)

def main():
        my_computer = Computer(
            "Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500
        )    
        my_computer.storeInformation()
        print(my_computer)

main()
