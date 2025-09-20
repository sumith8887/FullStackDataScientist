def add_item(items,item):
    items.append(item)
    print("Item added successfully into the menu.")
def remove_item(items,item):
    if(item not in items):
        print("Item is not present in the menu")
        return
    else:
        items.remove(item)
        print("Item removed successfully from the menu.")
def check_availability(items,item):
    if(item in items):
        print(f"Availability: {item} is available.")
    else:
        print(f"Availability: {item} is not available.")
def display_menu(items):
    print("Updated menu:",items)

items=eval(input("Enter the initial_menu : "))
while True:
    print("Menu\n1.Add an item\n2.Remove an item\n3.Check for availability of an item\n4.Display Menu\n5.Exit")
    try:
        ch=int(input("Enter your choice : "))
    except ValueError:
        print("Enter the integer value.")
        exit(1)
    if(ch<1 or ch>5):
        print("Please enter valid option between 1 and 5")
        exit(1)
    else:
        if(ch==1):
            item=input("Enter item to add in the menu : ")
            add_item(items,item)
        elif(ch==2):
            item=input("Enter item to delete in the menu : ")
            remove_item(items,item)
        elif(ch==3):
            item=input("Enter item to check availability in the menu : ")
            check_availability(items,item)
        elif(ch==4):
            display_menu(items)
        elif(ch==5):
            print("Thank you!Enjoy your meal.")
            exit(1)