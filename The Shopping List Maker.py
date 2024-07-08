# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")

def remove_item(shopping_list, item):
    try:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    except ValueError:
        print(f"{item} was not found in the shopping list.")

def print_list(shopping_list):
    print("\nShopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print()

def main():
    shopping_list = []
    while True:
        action = input("Would you like to add, remove, print the list, or quit? ").lower()
        if action == 'add':
            item_to_add = input("Enter the item to add: ")
            add_item(shopping_list, item_to_add)
        elif action == 'remove':
            item_to_remove = input("Enter the item to remove: ")
            remove_item(shopping_list, item_to_remove)
        elif action == 'print':
            print_list(shopping_list)
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose add, remove, print, or quit.")

if __name__ == "__main__":
    main()
