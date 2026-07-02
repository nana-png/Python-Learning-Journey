groceries = ["Milk", "Apple", "Banana", "Yoghurt", "Grape"]
while True:
    print(f"\n======================Grocery Store===================")
    print("1. View Grocery List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Unique Items")
    print("5. Search Item")
    print("6. Total Items")
    print("7. Items Starting with B")
    print("8. Exit")
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Invalid Option!")
        continue

    if option == 1:
        for num, item in enumerate(sorted(groceries), start=1):
            print(f"{num}. {item}")
    
    elif option == 2:
        item = input("Enter the item to add: ").title()
        groceries.append(item)
        print(f"{item} has been added to the grocery list.")
    
    elif option == 3:
        item = input("Enter the item to remove: ").title()
        if item in groceries:
            groceries.remove(item)
            print(f"{item} has been removed from the grocery list.")
        else:
            print(f"{item} is not in the grocery list.")
    
    elif option == 4:
        set_groceries = set(groceries)
        for i in set_groceries:
            print(i)

    elif option == 5:
        search = input("Enter the item you want to find: ").title()
        if search in groceries:
                print(f"Item Found!")
        else:
            print(f"Item not in grocery list!")

    elif option == 6:
        print(f"Total Groceres: {len(groceries)}")



    elif option == 7:
        for i in groceries:
            if i.startswith("B"):
                print(f"Items Starting with B: {i}")



    elif option == 8:
        
        break





