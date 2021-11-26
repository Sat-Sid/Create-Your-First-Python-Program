# ToDo application using Python3

user_input = "random"
data = []

def show_menu():
    print("1. Show all Todo list items")
    print("2. Add a new item to the list")
    print("3. Delete an item from the list")
    print("4. Exit the application")

while user_input != "4":
    show_menu()
    user_input = input("Enter your choice from the menu: ")

    if user_input == "1":
        for item in data:
            print(item)

    elif user_input == "2":
        new_item = input("What task need to be added? ")
        data.append(new_item)
        print(new_item,"has been added to your list")

    elif user_input == "3":
        delete_item = input("Which item need to be marked as done? ")
        
        if delete_item in data:
            data.remove(delete_item)
            print(delete_item, "has been deleted")
        else:
            print(delete_item, "does not exist")

    elif user_input == "4":
        print("GoodBye!")

    else:
        print("Choose the correct option from the menu")
