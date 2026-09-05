# Stock Portfolio Tracker

portfolio = {}

while True:
    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Calculate Total Value")
    print("4. Remove Stock")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Enter stock name: ").upper()
        shares = int(input("Enter number of shares: "))
        price = float(input("Enter price per share: "))

        portfolio[stock] = {
            "shares": shares,
            "price": price
        }

        print(f"{stock} added successfully!")

    elif choice == "2":
        if not portfolio:
            print("Portfolio is empty.")
        else:
            print("\n----- Your Portfolio -----")

            for stock, details in portfolio.items():
                value = details["shares"] * details["price"]

                print(
                    f"{stock}: "
                    f"{details['shares']} shares × "
                    f"${details['price']:.2f} = "
                    f"${value:.2f}"
                )

    elif choice == "3":
        total_value = 0

        for details in portfolio.values():
            total_value += details["shares"] * details["price"]

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    elif choice == "4":
        stock = input("Enter stock name to remove: ").upper()

        if stock in portfolio:
            del portfolio[stock]
            print(f"{stock} removed successfully!")
        else:
            print("Stock not found.")

    elif choice == "5":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")