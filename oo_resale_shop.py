from typing import Dict, Optional 
from computer import *
class ResaleShop:
   
    # What attributes will it need?
    inventory : Dict[int, Dict] = {}
    item_id = 0 
  
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                  inventory:Dict[int,Dict]):
        self.item_id = 0
        self.inventory = inventory

       
    # What methods will you need?
   
    def refurbish(self,item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id , "not found. Please select another item to refurbish.")

    def buy(self,computer):
        global itemID
        self.item_id += 1 # increment itemID
        self.item_id  = computer
        return self.item_id
    def printInventory(self,inventory):
        # If the inventory is not empty
        if inventory:
        # For each item
            for item_id in inventory:
                # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')
        else:
            print("No inventory to display.")
    def sell(self,item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

def main():
        Comp = Computer("Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500) 
        inventory : Dict[int, Dict] = {"description": Comp.description, "processor_type":Comp.processor_type, "hard_drive_capacity":Comp.hard_drive_capacity, "memory":Comp.memory, "operating_system":Comp.operating_system, "year_made":Comp.year_made, "price":Comp.price}
        shop = ResaleShop(inventory)
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

        # Add it to the resale store's inventory
        print("Buying", ["description"])
        print("Adding to inventory...")
        computer_id = shop.buy(Comp)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.printInventory(inventory)
        print("Done.\n")

        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        shop.refurbish(computer_id, new_OS)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.printInventory(inventory)
        print("Done.\n")
        
        # Now, let's sell it!
        print("Selling Item ID:", computer_id,inventory)
        shop.sell(computer_id)
        
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.printInventory(inventory)
        print("Done.\n")

# Calls the main() function when this file is run
main()