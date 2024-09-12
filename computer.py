class Computer:

    # What attributes will it need?
    # The attributes it will need are the description, processor type, hard drive capacity, operating system, year made, and price.
    # How will you set up your constructor?
    # I will use the self and set upt the attributes to the respective type.
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

    def main():
        my_computer = Computer(
            "Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500
        )
        print(my_computer)

    main()