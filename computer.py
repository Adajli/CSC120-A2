from computer import Any


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
        self.description = ""
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = 0
        self. operating_system = operating_system
        self.year_made = 0
        self.price = 0 

    # What methods will you need? 
    def attributes(self):
        return vars(self)
    
def main():
        my_computer = Computer(
            "Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500
        )    
         
        print(my_computer.attributes())

main()
