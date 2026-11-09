
# Day 19: Assignment 3 - Product Inventory Management
# Concepts: Lists, Dictionaries, Functions, Loops, Conditional Statements

# Store all product records in a list
products = []


def add_product():
    """Add a new product to inventory."""

    product_id = input("Enter Product ID: ").strip()

    # Check whether product ID already exists
    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    name = input("Enter Product Name: ").strip()

    try:
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Stock Quantity: "))

        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid price and quantity.")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully.")


def view_products():
    """Display all products."""

    if not products:
        print("Inventory is empty.")
        return

    print("\n--- Product Inventory ---")

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ₹{product['price']:.2f} | "
            f"Quantity: {product['quantity']}"
        )


def search_product():
    """Search for a product using its ID."""

    product_id = input("Enter Product ID to search: ").strip()

    for product in products:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Price: ₹{product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            return

    print("Product not found.")


def update_stock():
    """Update the stock quantity of a product."""

    product_id = input("Enter Product ID: ").strip()

    for product in products:
        if product["id"] == product_id:
            try:
                new_quantity = int(input("Enter New Stock Quantity: "))

                if new_quantity < 0:
                    print("Quantity cannot be negative.")
                    return

                product["quantity"] = new_quantity
                print("Stock updated successfully.")
                return

            except ValueError:
                print("Please enter a valid quantity.")
                return

    print("Product not found.")


def delete_product():
    """Delete a product from inventory."""

    product_id = input("Enter Product ID to delete: ").strip()

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully.")
            return

    print("Product not found.")


def inventory_summary():
    """Display inventory summary."""

    if not products:
        print("Inventory is empty.")
        return

    total_products = len(products)
    total_stock = sum(product["quantity"] for product in products)
    inventory_value = sum(
        product["price"] * product["quantity"]
        for product in products
    )

    print("\n--- Inventory Summary ---")
    print(f"Total Product Types: {total_products}")
    print(f"Total Stock Units: {total_stock}")
    print(f"Total Inventory Value: ₹{inventory_value:.2f}")


# Main program
while True:
    print("\n===== Product Inventory Management =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Inventory Summary")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        inventory_summary()

    elif choice == "7":
        print("Exiting Inventory Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 7.")
