# Cart for adding items
cart = []

# Start Page
def start_page():
    print("Welcome to the Vending Machine!")
    while True:
        choice = input("Do you want to use the vending machine? (yes/no): ").lower()
        if choice == "yes":
            main_menu()
            break
        elif choice == "no":
            goodbye()
            break
        else:
            print("Please enter 'yes' or 'no'.")
 
# Main Menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Drinks")
        print("2. Snacks")
        print("3. Checkout and Exit")
        choice = input("Choose a category (1/2/3): ")

        if choice == "1":
            drinks_menu()
        elif choice == "2":
            snacks_menu()
        elif choice == "3":
            checkout()
            break
        else:
            print("Invalid input, try again please.")

# Drinks Menu
def drinks_menu():
    drinks = ['Water - $1', 'Juice - $2', 'Coke - $3']
    while True:
        print("\nDrinks Menu:")
        for i, drink in enumerate(drinks, 1):
            print(f"{i}. {drink}")
        print("4. Go back to the main menu")

        choice = input("Select a drink (1-3) or go back (4): ")
        if choice in ['1', '2', '3']:
            selected_drink = drinks[int(choice) - 1]
            cart.append(selected_drink)
            print(f"{selected_drink} added to your cart!")
            confirm_purchase()
            break
        elif choice == "4":
            ask_to_switch("snacks")
            break
        else:
            print("Invalid input, please try again!")

# Snacks Menu
def snacks_menu():
    snacks = ["Chips - $1.50", "Chocolate Bar - $2.50", "Snack Bar - $3"]
    while True:
        print("\nSnacks Menu:")
        for i, snack in enumerate(snacks, 1):
            print(f"{i}. {snack}")
        print("4. Go back to the main menu")

        choice = input("Select a snack (1-3) or go back (4): ")
        if choice in ['1', '2', '3']:
            selected_snack = snacks[int(choice) - 1]
            cart.append(selected_snack)
            print(f"{selected_snack} added to your cart!")
            confirm_purchase()
            break
        elif choice == "4":
            ask_to_switch("drinks")
            break
        else:
            print("Invalid input, please try again!")

# Ask to Switch Menus
def ask_to_switch(menu_type):
    choice = input(f"Would you like to purchase anything from the {menu_type} menu? (yes/no): ").lower()
    if choice == "yes":
        if menu_type == "snacks":
            snacks_menu()
        elif menu_type == "drinks":
            drinks_menu()
    elif choice == "no":
        print("Proceeding to the checkout....")
        checkout()
    else:
        print("Invalid input. Proceeding to checkout!")
        checkout()

# Confirm Purchase
def confirm_purchase():
    while True:
        choice = input("\nConfirm purchase? (yes/no): ").lower()
        if choice == 'yes':
            checkout()
            break
        elif choice == 'no':
            print('Returning to the main menu...')
            main_menu()
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Checkout Function
def checkout():
    print("\nYour Cart:")

    if not cart:
        print("Your cart is empty. Returning you to the main menu...")
        main_menu()
        return

    total_cost = 0

    for item in cart:
        print(f"- {item}")
        price = float(item.split('$')[1])
        total_cost += price

    print(f"\nTotal Items: {len(cart)}")
    print(f"Total Cost: ${total_cost:.2f}")

    while True:
        try:
            cash = float(input("Enter cash amount: $"))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment successful! Your change is ${change:.2f}.")
                print("Thank you for completing your purchase!")
                goodbye()
                break
            else:
                print(f"Insufficient funds. You need ${total_cost - cash:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Goodbye Function
def goodbye():
    print("\nThank you for using Baig's Virtual Vending Machine!")
    print("We hope you enjoyed your experience!")
    print("Goodbye! See you soon!")


# This is a prompt to call the start page. (ignore)
if __name__ == "__main__":
    start_page()

