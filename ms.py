# Define a dictionary to store customer data
customers = {}

# Function to add a new customer
def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    customers[name] = {"email": email, "phone": phone}
    print(f"Customer {name} added successfully")

# Function to retrieve a customer's information
def get_customer():
    name = input("Enter customer name: ")
    customer = customers.get(name)
    if customer:
        print(f"Name: {name}, Email: {customer['email']}, Phone: {customer['phone']}")
    else:
        print(f"Customer {name} not found")

# Function to update a customer's information
def update_customer():
    name = input("Enter customer name: ")
    customer = customers.get(name)
    if customer:
        email = input("Enter new email (leave blank to keep current): ")
        phone = input("Enter new phone (leave blank to keep current): ")
        if email:
            customer['email'] = email
        if phone:
            customer['phone'] = phone
        print(f"Customer {name} updated successfully")
    else:
        print(f"Customer {name} not found")

# Function to delete a customer
def delete_customer():
    name = input("Enter customer name: ")
    if name in customers:
        del customers[name]
        print(f"Customer {name} deleted successfully")
    else:
        print(f"Customer {name} not found")

# Main loop
while True:
    print("\nMenu:")
    print("1. Add a new customer")
    print("2. Retrieve a customer's information")
    print("3. Update a customer's information")
    print("4. Delete a customer")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ")
    if choice == "1":
        add_customer()
    elif choice == "2":
        get_customer()
    elif choice == "3":
        update_customer()
    elif choice == "4":
        delete_customer()
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again")
