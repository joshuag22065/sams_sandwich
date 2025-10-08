import datetime

def force_number(message, lower, upper, allow_enter=False):
    while True:
        user_input = input(message)
        if allow_enter and user_input == "":  # only allowed when specifically enabled
            return ""
        else:
            try:
                num = int(user_input)
                if lower <= num <= upper:
                    return num
                else:
                    print(f"The number {num} is wrong, please type in a number between {lower}-{upper}")
            except ValueError:
                print("Error, please enter in a number")

def force_cellphone_number(message, lower, upper):  # Force string cellphone number
    while True:
        cell = input(message).strip()
        if lower <= len(cell) <= upper and cell.isnumeric():
            return cell
        else:
            print(f"ERROR! Please enter a number between {lower} - {upper} characters (digits only)")

def force_name(message, lower=2, upper=20):  # Force name for inputs
    while True:
        name = str(input(message)).title().strip()
        if lower <= len(name) <= upper and name.isalpha():
            return name
        else:
            print(f"Try a name between {lower}-{upper} characters (letters only)")

def bread_selection(): # Selects the bread
    bread_list = ["White", "Brown", "Italian", "Granary"]
    print_list(bread_list, "breads")
    bread_selected = force_number(("Which bread do you want? Enter a number: "), 1, len(bread_list))
    return bread_list[bread_selected-1] #Returns back a string

def print_list(list, item):
    count = 0
    print(f"We have the following {item}: ")
    while count < len(list): #prints out each item on the list
        print(count+1, " ",list[count])
        count +=1
    return

def meat_selection():
    meat_list = ["Salami", "Chicken Strips","Bacon", "Pork Ribs", "Ham", "Tofu"]
    print_list(meat_list, "meats")
    meat_selected = force_number(("Which meat do you want? Enter a number: "), 1, len(meat_list))
    return meat_list[meat_selected-1] #Returns back a string

def cheese_selection():
    cheese_list = ["Swiss", "Cheddar","Edam", "Blue Cheese", "Brie", "Feta"]
    print_list(cheese_list, "cheeses")
    cheese_selected = force_number(("Which cheese do you want? Enter a number: "), 1, len(cheese_list))
    return cheese_list[cheese_selected-1] #Returns back a string

def salad_selection():
    salad_list = ["Lettuce", "Corn","Tomato", "Spinach", "Peppers", "Jalapeños"]
    print_list(salad_list, "salads")
    print("Press ENTER when you have finished choosing your salads")
    salads_added = "" # Will hold a string of more than one item
    selected_salad= " " # Promps the user to enter a number in to select a salad

    while selected_salad != "": # If enter is not pressed it will keep prompting you to select a salad
        selected_salad =  force_number((f"What number salad do you want? Enter a number: "), 1, len(salad_list), allow_enter=True)
        if selected_salad != "" :# If you press enter this if statement wont run
            selected_salad= int(selected_salad)
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip() # Removes empty space at the start of the string

def sauce_selection():
    sauce_list = [" Regular Mayonnaise", " Oil"," Red Wine Vinegar", " Yellow Mustard", " Honey Mustard", " Cheddar sauce", " BBQ", " Siracha", " Mariana Sauce", "Sweet Onion Teriyaki", "Peppercorn Ranch"]
    count = 0
    print("We have the following sauce: ")
    while count < len(sauce_list): #prints out each item on the list
        print(count+1, "", sauce_list[count])
        count +=1
    sauce_selected = force_number(("Which sauce do you want? Enter a number: "), 1, len(sauce_list))
    return sauce_list[sauce_selected-1].strip() #Returns back a string

def output_textfile(sandwich_order):
    date_time = datetime.datetime.now()
    outF=open("Sam's_sandwiches.txt", "a")
    print(" \n***The quote for the sandwich***")
    outF.write(f"\n ************NEW ORDER RECIEVED************")
    outF.write(f"\nDate of booking: {date_time}")
    for booking in sandwich_order:
        print (booking)
        outF.write(f"\n {booking}") #outputs each item to the text file
    outF.write(f" \n************END OF ORDER************ \n")
    outF.close()

#Main program
phone_number = force_cellphone_number('Please enter in your phone number: ', 6,10)
first_name = force_name("Please enter in your first name: ")
print("Welcome to Sam's Sandwich Shop")
bread_choice=bread_selection() # Creating a variable that calls up the bread function and  returns their choice
print(f"Your selected bread: {bread_choice}")
meat_choice=meat_selection() # Creating a variable that calls up the meat function and  returns their choice
print(f"Your selected meat: {meat_choice}")
cheese_choice=cheese_selection() # Creating a variable that calls up the meat function and  returns their choice
print(f"Your selected cheese: {cheese_choice}")
salad_choice=salad_selection() # Creating a variable that calls up the meat function and  returns their choice
print(f"Your selected salads: {salad_choice}")
sauce_choice=sauce_selection() # Creating a variable that calls up the meat function and  returns their choice
print(f"Your selected sauce: {sauce_choice}")
sandwich_order=[] #Appending choices to list to be printed out
sandwich_order.append(f"Bread: {bread_choice}") 
sandwich_order.append(f"Meat: {meat_choice}") 
sandwich_order.append(f"Cheese: {cheese_choice}") 
sandwich_order.append(f"Salad: {salad_choice}") 
sandwich_order.append(f"Sauce: {sauce_choice}")
output_textfile(sandwich_order)