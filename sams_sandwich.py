# imports the date and time function 
import datetime 

#This program will allow the user to enter in a name
def force_name(message,lower,upper):
   #This is an infinite loop that will only break if a valid name is entered
    while True:
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            break #the loop bresks if the above condition is met
        else:
            print(f"Invalid name. Your name must have no numbers or characters and be between {lower} and {upper} characters long")
    return name #a valid name is returned back to the variable that called the function

#The purpose of this function is to enter in a valid number
def force_number(message,lower,upper,allow_enter=False):
    while True: #infinite loop that keeps repeating until a valid number is entered
        try:
            # this part checks if it is the salad option which means you push enter to end
            num=(input(message)) 
            if num == "" and allow_enter==True:
                return
            # and if its not it turns it into an interger and checks it is in a valid range
            else:
                num=(int(num))
            if num>=lower and num<=upper:
                break
            # prints different error statements based on what is allowed by that variable
            else:
                if allow_enter==True:
                    print(f"Incorrect, you must select a number between {lower} and {upper} or press enter")
                else:
                    print(f"Incorrect, you must select a number between {lower} and {upper}")
        except: #this will only print if you type in a string
            print("Error, please enter in a number not text")
    return num #returning back a valid number within a range

def force_phone(message,lower,upper):
    # this is to check the phone number is the right length and is a number
    while True:
        num=input(message)
        if len(num) >= lower and len(num) <= upper and num.isnumeric():
            break
        else:
            print(f"Error! Please enter a phone number in length between {lower} and {upper}.")
    return num

def print_list(list, item):
    # this code prints all of the options stored in each categories list 
    count = 0
    print(f"We have the following {item}: ")
    while count < len(list):
        print(count+1," - ",list[count])
        count += 1

# the following have the variables, print the list of options available using seperate function then it returns it to main program 
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    print_list(bread_list,"breads")
    bread_selected = force_number("Which bread did you want? Enter a number: ",1,len(bread_list))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list = ["Chicken Strips", "Chicken Patty", "Steak", "Meatballs", "Teriyaki Chicken", "Vegetable Patty", "Bacon", "Salami", "Ham", "Falafal", "Pork Riblet", "Tuna", "Popcorn Chicken", "Roast Beef", "Corned beef", "No meat"]
    print_list(meat_list,"meats")
    meat_selected = force_number("What meat did you want? Enter a number: ",1,len(meat_list))
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list = ["Cheddar", "Smoked", "Mozzarella", "Swiss", "Feta", "Vegan Cheese", "No Cheese"]
    print_list(cheese_list,"cheeses")
    cheese_selected = force_number("What cheese did you want? Enter a number: ",1,len(cheese_list))
    return cheese_list[cheese_selected-1]

# this is slightly different as it allows you to choose as many as you want and push enter when you are done 
def salad_selection(): 
    salad_list = ["Lettuce", "Spinach", "Tomato", "Cucumber", "Pickles", "Capsicum", "Olives", "Red Onion", "Jalapeños", "Carrot", "Potato", "NO SALAD"]
    print_list(salad_list,"salads")
    print("Press ENTER when you have finished choosing your salads")
    
    salad_choice = []
    while True: #infinite loop
        salad_option=force_number(f"What number salad do you want?\nYou have selected {', '.join(salad_choice)} so far\nEnter number: ",1,len(salad_list),allow_enter=True)
        if salad_option == "":
            break
        else:
            salad_choice.append(salad_list[salad_option-1])
    return ", ".join(salad_choice)

def dressing_selection():
    dressing_list = ["Tomato Sauce", "Mustard", "Mexican Salsa", "Smoky BBQ Sauce", "Caesar Dressing", "Chipotle Sauce", "Spicy Mayonnaise", "Habanero Hot Sauce", "Honey Mustard Sauce", "Marinara Sauce", "Mayonnaise", "Ranch Dressing", "Sweet Onion Sauce", "Garlic Aioli Sauce", "Sweet Chilli Sauce"]
    count = 0
    print_list(dressing_list,"dressings")
    dressing_selected = force_number("What dressing did you want? Enter a number: ",1,len(dressing_list))
    return dressing_list[dressing_selected-1]

# outputs to textfile which could be sent to a reciept printer etc if needed 
def output_text_file(sandwich_order):
    outF = open("orders.txt", "a") #Opens the bookings text file
    outF.write(f"\n\n*****NEW ORDER RECIEVED**********\n") #Opening statement in text file
    outF.write(f"\nDate created:{date_time}")
    for order_piece in sandwich_order: #For every ticket order
        outF.write(f"\n{order_piece}") #Prints out the students on a new line
        print(order_piece)
    outF.write("\n*************ORDER ENDS**************\n\n")
    outF.close() #Closes the bookings text file
    print("Booking sent to store - pickup in 15 minutes") #test print statement

#main program
# this gets all of the information
print("Welcome to Sam's Sandwich Shop")
categories = [("name", force_name("What is your name: ",2,15)), ("phone number", force_phone("What is your phone number in NZ Format: ",9,12)), ("selected bread", bread_selection()), ("selected meat", meat_selection()), ("selected cheese", cheese_selection()), ("selected salads", salad_selection()), ("selected dressing", dressing_selection())]
count = 0
sandwich_order = []
date_time = datetime.datetime.now()
sandwich_order.append(date_time)
for category, func in categories:
    choice = func
    sandwich_order.append(f"Your {category}: {choice}\n")

output_text_file(sandwich_order)