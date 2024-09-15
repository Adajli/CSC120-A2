class ResaleShop:
    from typing import Dict, Optional 
   
    # What attributes will it need?
    inventory : Dict[int, Dict] = {}
    itemID = 0 
    item_id: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, item_id: int,
                  inventory:Dict[int,Dict], computer):
        self.item_id = 0
        self.inventory = {}
        import computer
        self.computer = computer(self)

    # What methods will you need?
   
    def refurbish(self,inventory,item_id: int, new_os: Optional[str] = None):
        if item_id in inventory:
            computer = inventory[item_id] # locate the computer
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
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def buy(self,computer):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[itemID] = computer
        return itemID
    def printInventory(self,inventory):
        # If the inventory is not empty
        if inventory:
        # For each item
            for item_id in inventory:
                # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id].attributes}')
        else:
            print("No inventory to display.")
def main():
     object = ResaleShop._init_(
        ) 
        
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = computer.buy()
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computer.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    computer.print("Checking inventory...")
    computer.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    computer.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computer.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
main()