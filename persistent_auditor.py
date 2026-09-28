""" 
INF1103 Week 4 - Persistent Auditor
"""

#Global Constant
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate
INVENTORY_FILE = "inventory.txt"

# Load the saved inventory, transaction history
def load_inventory():
    inventory=[]
    try: 
        with open("inventory.txt", "r") as f:
            for line in f: #Read file one line at a time
                parts = line.strip().split(",")
                order = (int(parts[0]),parts[1],int(parts[2]))
                inventory.append(order)
            last_id = inventory[-1][0]                                                                                 
            return inventory, last_id  
    except FileNotFoundError:
        return [],1000
    
def save_inventory(inventory):
    with open("inventory.txt", "w") as f:
        for order in inventory:
            f.writes(str(order[0]) + "," + order[1] + "," + str(order[2]) + "\n")


# Write inventory, transaction history.
def save_inventory(inventory, transaction_history):
    return None #return nothing

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
    inventory = 0
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



    

