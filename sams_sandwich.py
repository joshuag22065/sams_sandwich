import datetime

def force_number(message,lower,upper):
    while True: #Infinite loop that loops until valid number is entered
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break
            else:
                print(f"The number {num} is wrong, please type in a number between {lower}-{upper}")
        except: #Only prints when users type in a string
            print("Error, please enter in a number")
    return num #Returns back valid number

def bread_selection(): # Selects the bread
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count = 0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1, " ", bread_list[count])
        count +=1
    bread_selected = force_number(("Which bread do you want? Enter a number: "), 1, len(bread_list))
    return bread_list[bread_selected-1] #Returns back a string

def meat_selection():
    meat_list = ["Salami", "Chicken Strips","Bacon", "Pork Ribs", "Ham", "Tofu"]
    count = 0
    print("We have the following meats: ")
    while count < len(meat_list): #prints out each item on the list
        print(count+1, " ", meat_list[count])
        count +=1
    meat_selected = force_number(("Which meat do you want? Enter a number: "), 1, len(meat_list))
    return meat_list[meat_selected-1] #Returns back a string

def cheese_selection():
    cheese_list = ["Swiss", "Cheddar","Edam", "Blue Cheese", "Brie", "Feta"]
    count = 0
    print("We have the following cheeses: ")
    while count < len(cheese_list): #prints out each item on the list
        print(count+1, " ", cheese_list[count])
        count +=1
    cheese_selected = force_number(("Which cheese do you want? Enter a number: "), 1, len(cheese_list))
    return cheese_list[cheese_selected-1] #Returns back a string

def salad_selection():
    salad_list = ["Lettuce", "Corn","Tomato", "Spinach", "Peppers", "Jalapeños"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count < len(salad_list):
        print(count+1, " ", salad_list[count])
        count +=1
    print("Press ENTER when you have finished choosing your salads")
    salads_added = "" # Will hold a string of more than one item
    selected_salad= " " # Promps the user to enter a number in to select a salad

    while selected_salad != "": # If enter is not pressed it will keep prompting you to select a salad
        selected_salad =  force_number((f"What number salad do you want? Enter a number: "), 1, len(salad_list))
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
    print("***The quote for the sandwich***")
    outF.write(f"\nDate of booking: {date_time}")
    for booking in sandwich_order:
        print (booking)
        outF.write(f"\n {booking}") #outputs each item to the text file
    print("***End of quote***")
    outF.close()

#Main program
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
#This is temporay code to test that the bread subroutine is working first_name=str(input("What is your first name?")) cell_phone=str(input("What is your cellphone?")) bread_choice=bread_selection() meat_choice=meat_selected)
sandwich_order=[] #empty list #adding selected items to the list sandwhich_order.append(first_name) sandwhich_order.append(cell_phone)
sandwich_order.append(f"Bread: {bread_choice}") 
sandwich_order.append(f"Meat: {meat_choice}") 
sandwich_order.append(f"Cheese: {cheese_choice}") 
sandwich_order.append(f"Salad: {salad_choice}") 
sandwich_order.append(f"Sauce: {sauce_choice}")
output_textfile(sandwich_order)