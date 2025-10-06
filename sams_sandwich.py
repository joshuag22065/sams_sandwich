def bread_selection(): # Selects the bread
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count = 0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1, " ", bread_list[count])
        count +=1
    bread_selected = int(input("Which bread do you want? Enter a number: "))
    return bread_list[bread_selected-1] #Returns back a string

def meat_selection():
    meat_list = ["Salami", "Chicken Strips","Bacon", "Pork Ribs", "Ham", "Tofu"]
    count = 0
    print("We have the following meats: ")
    while count < len(meat_list): #prints out each item on the list
        print(count+1, " ", meat_list[count])
        count +=1
    meat_selected = int(input("Which meat do you want? Enter a number: "))
    return meat_list[meat_selected-1] #Returns back a string

def cheese_selection():
    cheese_list = ["Swiss", "Cheddar","Edam", "Blue Cheese", "Brie", "Feta"]
    count = 0
    print("We have the following cheeses: ")
    while count < len(cheese_list): #prints out each item on the list
        print(count+1, " ", cheese_list[count])
        count +=1
    cheese_selected = int(input("Which cheese do you want? Enter a number: "))
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
        selected_salad =  input(f"What number salad do you want? Enter a number: ")
        if selected_salad != "" :# If you press enter this if statement wont run
            selected_salad= int(selected_salad)
            #this variable keeps adding on each selected item from the salad list
            salads_added = salads_added + " " + salad_list[selected_salad]
        return salads_added.strip() # Removes empty space at the start of the string
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