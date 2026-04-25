#task 11 Inventory Manager

# Product Inventory System

products = {}

while True:
    print("------ MENU ------")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Show Low Stock (<5)")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        products.update({name:qty})
        print("Product added!")

    elif choice == 2:
        name = input("Enter product name: ")
        if name in products:
            qty = int(input("Enter new quantity: "))
            products[name] = qty
            print("Quantity updated!")
        else:
            print("Product not found!")

    elif choice == 3:
        name = input("Enter product name to remove: ")
        if name in products:
            del products[name]
            print("Product removed!")
        else:
            print("Product not found!")

    elif choice == 4:
        name = input("Enter product name to search: ")
        if name in products:
            print(name, "quantity:", products[name])
        else:
            print("Product not found!")

    elif choice == 5:
        print("Low stock products:")
        for item in products:
            if products[item] < 5:
                print(item, ":", products[item])

    elif choice == 6:
        break

    else:
        print("Invalid choice")