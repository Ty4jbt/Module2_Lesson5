# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1
def add_to_list(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

# Task 2
def remove_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

# Task 3
def show_list(shopping_list):
    if not shopping_list:
        return "The shopping list is empty."
    else:
        print("Shopping List: ")
        for item in shopping_list:
            print(f'{item}')

# Actual shopping list application
def manage_shopping_list():

    # Initialize the shopping list
    shopping_list = []

    # Creates endless loop until user decides to quit
    while True:

        # Gives user options to add, remove, print, or quit
        action = input('Enter "add" to add an item, "remove" to remove an item, "print" to display the list, or "quit" to exit: ').lower()
        
        # Incorporates the add function
        if action == "add":
            item = input("Enter the item you want to add: ")
            add_to_list(shopping_list, item)
            print(f"{item} has been added to the list.")
        
        # Incorporates the remove function
        elif action == "remove":
            item = input("Enter the item you want to remove: ")
            remove_from_list(shopping_list, item)
            print(f"{item} has been removed from the list.")

        # Incorporates the print function
        elif action == "print":
            show_list(shopping_list)

        # Uses break to end loop and quit the program
        elif action == "quit":
            break

        # Catches invalid actions
        else:
            print("Invalid action. Please try again.")