""" 
INF1103 Week 4 - Persistent Auditor
"""

#Global Constant
EXIT_SIGNAL = -99
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate
INVENTORY_FILE = "inventory.txt"

# Inventory item structure
ITEM_FIELDS = {
 "id": 0,
 "name": 1,
 "quantity": 2,
 "transaction_history": 3
}
FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"

# Load the saved inventory, transaction history
def load_inventory():
    inventory=[]
    transaction_history = []
    try: 
        with open("inventory.txt", "r") as f:
            for line in f: #Read file one line at a time
                parts = line.strip().split(FIELD_SEPARATOR)
                history= list(map(int, parts[3].split(HISTORY_SEPARATOR)))  
                item = (int(parts[0]), parts[1], int(parts[2]), history)                         
                inventory.append(item)                                                           
                transaction_history.extend(history)                                                                                      
            return inventory, transaction_history  
    except FileNotFoundError:
        return [], []
    
def save_inventory(inventory, transaction_history):
      with open(INVENTORY_FILE, "w") as f:
        for item in inventory:
            history_str = HISTORY_SEPARATOR.join(str(x) for x in transaction_history)
            total = sum(transaction_history)
            f.write(str(item[0]) + FIELD_SEPARATOR + item[1] + FIELD_SEPARATOR + str(total) + FIELD_SEPARATOR + history_str + "\n")

def get_valid_input():
    userInput = input("Enter stock quantity or 'quit' to exit: ")

    if userInput == "quit":
        return "quit"
    elif not userInput.lstrip('-').isdigit():
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit")
        return ("Invalid")
    elif int(userInput) <0:
        print("Please enter a positive number.")
        return("Invalid")
    else:
        return int(userInput)

def calculate_tax(amount):
    tax_amount = amount * TAX_RATE
    return tax_amount

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def generate_report(total_units, failed_attempts):
    print("Exiting the program. " + "Total units processed: " + str(total_units) + ". Number of failed attempts: " + str(failed_attempts) )

def main():
    """
    Main function to run inventory auditor program.
    """

    # local variables
    inventory = []
    tax_amount = 0
    exit_program = False
    failed_attempts = 0
    while not exit_program:

        response = get_valid_input()
        if response == "Invalid":
            failed_attempts+=1
        elif response == "quit":
            generate_report(inventory, failed_attempts)
            exit_program = True
        else:
            # overstock check goes here, before updating inventory                                                                                
            if inventory + response > MAX_CAPACITY:                                                                                               
                failed_attempts += 1                                                                                                              
                print("Overstock alert! You cannot add " + str(response) + " items. Maximum capacity is " + str(MAX_CAPACITY) + ".")    
                exit_program = True          
            else:                                                                                                                                 
                inventory = process_delivery(inventory, response)                                                                                 
                tax_amount = calculate_tax(inventory)                                                                                             
                print("Added " + str(response) + " items. Total: " + str(inventory) + " Tax: $" + str(tax_amount))          

# __name__ (Program Entry Point)
if  __name__=="__main__":
    main()



    

